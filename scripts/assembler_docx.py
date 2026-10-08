#!/usr/bin/env python3
"""Assemble le document de configuration Word à partir du gabarit.

Usage :
  python scripts/assembler_docx.py corps.md --client "Client" --salle "Salle 308" \
      --type-salle "Salle de formation" --sortie Client_Salle308_Configuration.docx

corps.md est le contenu déjà assemblé (variables résolues), en Markdown simple :
titres #/##/###, paragraphes, **gras**, *italique*, listes « - » et « 1. »,
tableaux à barres verticales, images ![alt](chemin). Les commentaires HTML sont
ignorés. Les chemins d'image sont relatifs au fichier corps.md ou au dossier du skill.
"""
import argparse, datetime, os, re, struct, sys, zipfile
from xml.sax.saxutils import escape

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ABSTRACT_DECIMAL = "21"   # liste numérotée « 1. » du gabarit
NUM_PUCES = "25"          # liste à puces du gabarit
LARGEUR_MAX = 5943600     # 6,5 po en EMU
HAUTEUR_MAX = 5486400     # 6 po
POLICE = '<w:rFonts w:ascii="Argumentum" w:hAnsi="Argumentum"/>'
TEXTES = {
    "fr": {"toc_title": "Contenus", "missing": "[À COMPLÉTER : NAME]",
           "toc_hint": "Mettre à jour la table des matières (clic droit, Mettre à jour les champs)."},
    "en": {"toc_title": "Contents", "missing": "[TO COMPLETE: NAME]",
           "toc_hint": "Update the table of contents (right-click, Update Field)."},
}
A_COMPLETER = re.compile(r"(\[(?:À COMPLÉTER|TO COMPLETE)[^\]]*\])")


def runs(texte, gras=False, police=False):
    """Convertit le Markdown en ligne (**gras**, *italique*) en runs Word."""
    texte = re.sub(r"<(https?://[^>]+)>", r"\1", texte).replace("\\*", "\u0001").replace("\\$", "$")
    out = []
    for morceau in re.split(r"(\*\*\*.+?\*\*\*|\*\*.+?\*\*|\*.+?\*)", texte):
        if not morceau:
            continue
        b, i = gras, False
        if morceau.startswith("***") and morceau.endswith("***") and len(morceau) > 6:
            b, i, morceau = True, True, morceau[3:-3]
        elif morceau.startswith("**") and morceau.endswith("**") and len(morceau) > 4:
            b, morceau = True, morceau[2:-2]
        elif morceau.startswith("*") and morceau.endswith("*") and len(morceau) > 2:
            i, morceau = True, morceau[1:-1]
        for part in A_COMPLETER.split(morceau):
            if not part:
                continue
            manque = bool(A_COMPLETER.fullmatch(part))
            rpr = (POLICE if police else "") + ("<w:b/><w:bCs/>" if b or manque else "") + \
                  ("<w:i/><w:iCs/>" if i else "") + ('<w:highlight w:val="yellow"/>' if manque else "")
            part = part.replace("`", "").replace("\u0001", "*")
            out.append('<w:r>%s<w:t xml:space="preserve">%s</w:t></w:r>' % (
                "<w:rPr>%s</w:rPr>" % rpr if rpr else "", escape(part)))
    return "".join(out)


def taille_image(chemin):
    with open(chemin, "rb") as f:
        d = f.read()
    if d[:8] == b"\x89PNG\r\n\x1a\n":
        return struct.unpack(">II", d[16:24])
    i = 2  # JPEG
    while i < len(d):
        if d[i] != 0xFF:
            i += 1
            continue
        m = d[i + 1]
        if 0xC0 <= m <= 0xCF and m not in (0xC4, 0xC8, 0xCC):
            h, w = struct.unpack(">HH", d[i + 5:i + 9])
            return w, h
        i += 2 + struct.unpack(">H", d[i + 2:i + 4])[0]
    raise ValueError("Format d'image non reconnu : " + chemin)


class Corps:
    def __init__(self, base):
        self.base, self.xml, self.images, self.nums = base, [], [], []
        self.prochain_num, self.num_courant, self.id_dessin = 900, None, 9000
        self.avertissements = []

    def titre(self, niveau, texte):
        self.xml.append('<w:p><w:pPr><w:pStyle w:val="Titre%d"/>%s</w:pPr>%s</w:p>' % (
            min(niveau, 3), '<w:ind w:left="0" w:firstLine="0"/>' if niveau == 1 else "", runs(texte, police=True)))

    def paragraphe(self, texte):
        self.xml.append('<w:p><w:pPr><w:spacing w:before="0" w:after="200"/></w:pPr>%s</w:p>' % runs(texte, police=True))

    def item(self, texte, numero=None):
        if numero is None:
            num = NUM_PUCES
        else:
            if numero == 1 or self.num_courant is None:
                self.num_courant = str(self.prochain_num)
                self.prochain_num += 1
                self.nums.append('<w:num w:numId="%s"><w:abstractNumId w:val="%s"/><w:lvlOverride w:ilvl="0">'
                                 '<w:startOverride w:val="%d"/></w:lvlOverride></w:num>' % (self.num_courant, ABSTRACT_DECIMAL, numero))
            num = self.num_courant
        self.xml.append('<w:p><w:pPr><w:pStyle w:val="Paragraphedeliste"/><w:numPr><w:ilvl w:val="0"/>'
                        '<w:numId w:val="%s"/></w:numPr></w:pPr>%s</w:p>' % (num, runs(texte)))

    def tableau(self, lignes):
        n = max(len(l) for l in lignes)
        lignes = [l + [""] * (n - len(l)) for l in lignes]
        large = n > 4
        brut = lambda t: re.sub(r"[*`]", "", t)
        # largeur des colonnes proportionnelle au contenu, bornée à la largeur de la page
        if large:  # tableau large : petite police, colonnes selon le mot le plus long, débord permis dans les marges
            ws = [max(480, max(len(m) for l in lignes for m in (brut(l[c]).split() or [""])) * 82 + 200) for c in range(n)]
            limite = 10800
        else:
            ws = [max(900, min(4200, max(len(brut(l[c])) for l in lignes) * 125 + 300)) for c in range(n)]
            limite = 9360
        if sum(ws) > limite:
            ws = [w * limite // sum(ws) for w in ws]
        petit = '<w:sz w:val="14"/><w:szCs w:val="14"/>' if large else ""
        x = ['<w:tbl><w:tblPr><w:tblStyle w:val="Grilledutableau"/><w:tblW w:w="%d" w:type="dxa"/><w:jc w:val="center"/>'
             '<w:tblLook w:val="04A0" w:firstRow="1" w:lastRow="0" w:firstColumn="1" w:lastColumn="0" w:noHBand="0" w:noVBand="1"/>'
             '</w:tblPr><w:tblGrid>%s</w:tblGrid>' % (sum(ws), "".join('<w:gridCol w:w="%d"/>' % w for w in ws))]
        for r, ligne in enumerate(lignes):
            x.append('<w:tr><w:trPr>%s<w:jc w:val="center"/></w:trPr>' % ("<w:tblHeader/>" if r == 0 and large else ""))
            for c in range(n):
                gras = (r == 0) or (c == 0 and not large)
                contenu = runs(ligne[c], gras=gras)
                if petit:
                    contenu = contenu.replace("<w:r><w:rPr>", "<w:r><w:rPr>" + petit).replace("<w:r><w:t", "<w:r><w:rPr>%s</w:rPr><w:t" % petit)
                fond = '<w:shd w:val="clear" w:color="auto" w:fill="D9D9D9"/>' if r == 0 and large else ""
                x.append('<w:tc><w:tcPr><w:tcW w:w="%d" w:type="dxa"/>%s</w:tcPr><w:p><w:pPr><w:spacing w:before="0" w:after="0"/>'
                         '<w:jc w:val="%s"/></w:pPr>%s</w:p></w:tc>' % (ws[c], fond, "left" if large else "center", contenu))
            x.append("</w:tr>")
        x.append('</w:tbl><w:p><w:pPr><w:spacing w:before="0" w:after="0"/></w:pPr></w:p>')
        self.xml.append("".join(x))

    def image(self, alt, chemin):
        for racine in (self.base, RACINE, os.path.join(RACINE, "references"), os.path.join(RACINE, "references", "fr")):
            p = os.path.normpath(os.path.join(racine, chemin))
            if os.path.isfile(p):
                break
        else:
            self.avertissements.append("Image introuvable, omise : " + chemin)
            return
        wpx, hpx = taille_image(p)
        cx = min(LARGEUR_MAX, wpx * 9525)
        cy = round(cx * hpx / wpx)
        if cy > HAUTEUR_MAX:
            cx, cy = round(HAUTEUR_MAX * wpx / hpx), HAUTEUR_MAX
        ext = os.path.splitext(p)[1].lower().lstrip(".")
        nom = "cfg_image%d.%s" % (len(self.images) + 1, ext)
        rid = "rIdCfg%d" % (len(self.images) + 1)
        self.images.append((rid, nom, p))
        self.id_dessin += 1
        self.xml.append(
            '<w:p><w:pPr><w:spacing w:before="0" w:after="200"/><w:jc w:val="center"/></w:pPr><w:r><w:drawing>'
            '<wp:inline distT="0" distB="0" distL="0" distR="0"><wp:extent cx="%d" cy="%d"/><wp:docPr id="%d" name="%s" descr="%s"/>'
            '<a:graphic xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main"><a:graphicData uri="http://schemas.openxmlformats.org/drawingml/2006/picture">'
            '<pic:pic xmlns:pic="http://schemas.openxmlformats.org/drawingml/2006/picture"><pic:nvPicPr><pic:cNvPr id="%d" name="%s"/><pic:cNvPicPr/></pic:nvPicPr>'
            '<pic:blipFill><a:blip r:embed="%s"/><a:stretch><a:fillRect/></a:stretch></pic:blipFill>'
            '<pic:spPr><a:xfrm><a:off x="0" y="0"/><a:ext cx="%d" cy="%d"/></a:xfrm><a:prstGeom prst="rect"><a:avLst/></a:prstGeom></pic:spPr>'
            '</pic:pic></a:graphicData></a:graphic></wp:inline></w:drawing></w:r></w:p>'
            % (cx, cy, self.id_dessin, nom, escape(alt, {'"': "&quot;"}), self.id_dessin, nom, rid, cx, cy))


def convertir(md, base):
    c = Corps(base)
    md = re.sub(r"<!--.*?-->", "", md, flags=re.S)
    lignes = md.splitlines()
    i, para = 0, []

    def vider():
        if para:
            c.paragraphe(" ".join(para))
            para.clear()

    while i < len(lignes):
        l = lignes[i].rstrip()
        s = l.strip()
        m_img = re.fullmatch(r"!\[([^\]]*)\]\(([^)]+)\)", s)
        m_num = re.match(r"(\d+)\.\s+(.*)", s)
        if not s:
            vider()
        elif s.startswith("#"):
            vider()
            niveau = len(s) - len(s.lstrip("#"))
            c.titre(niveau, s.lstrip("#").strip())
            c.num_courant = None
        elif m_img:
            vider()
            c.image(m_img.group(1), m_img.group(2))
        elif s.startswith("|"):
            vider()
            rangs = []
            while i < len(lignes) and lignes[i].strip().startswith("|"):
                cellules = [x.strip() for x in re.split(r"(?<!\\)\|", lignes[i].strip().strip("|"))]
                if not all(re.fullmatch(r":?-{2,}:?", x) for x in cellules):
                    rangs.append(cellules)
                i += 1
            c.tableau(rangs)
            continue
        elif m_num:
            vider()
            c.item(m_num.group(2), int(m_num.group(1)))
        elif re.match(r"[-*]\s+", s):
            vider()
            c.item(re.sub(r"^[-*]\s+", "", s))
        else:
            para.append(s)
        i += 1
    vider()
    return c


def main():
    a = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    a.add_argument("corps")
    a.add_argument("--lang", choices=("fr", "en"), default="fr", help="langue du document (défaut : fr)")
    a.add_argument("--client", required=True)
    a.add_argument("--salle", "--room", dest="salle", required=True)
    a.add_argument("--type-salle", "--room-type", dest="type_salle", default="",
                   help="texte de l'en-tête après le client (défaut : la salle)")
    a.add_argument("--revision", default="1.0")
    a.add_argument("--date", default=datetime.date.today().isoformat(), help="AAAA-MM-JJ")
    a.add_argument("--gabarit", default=os.path.join(RACINE, "assets", "gabarit.docx"))
    a.add_argument("--sortie", "--output", dest="sortie", required=True)
    o = a.parse_args()

    d = datetime.date.fromisoformat(o.date)
    champs = {"{{CLIENT}}": o.client, "{{ROOM}}": o.salle, "{{ROOM_TYPE}}": o.type_salle or o.salle,
              "{{TOC_TITLE}}": TEXTES[o.lang]["toc_title"], "{{TOC_HINT}}": TEXTES[o.lang]["toc_hint"],
              "{{REVISION}}": o.revision, "{{DATE}}": "%d/%d/%d" % (d.month, d.day, d.year)}
    with open(o.corps, encoding="utf-8") as f:
        c = convertir(f.read(), os.path.dirname(os.path.abspath(o.corps)))

    reste = sorted(set(re.findall(r"\{\{[^}]*\}\}", "".join(c.xml))))
    if reste:
        sys.exit("Variables non résolues dans le corps : " + ", ".join(reste) +
                 "\nLes remplacer par une valeur ou par %s avant d'assembler." % TEXTES[o.lang]["missing"])

    zin = zipfile.ZipFile(o.gabarit)
    zout = zipfile.ZipFile(o.sortie, "w", zipfile.ZIP_DEFLATED)
    for info in zin.infolist():
        data = zin.read(info.filename)
        if info.filename.endswith((".xml", ".rels")):
            t = data.decode("utf-8")
            for k, v in champs.items():
                t = t.replace(k, escape(v))
            if info.filename == "word/document.xml":
                t = re.sub(r"<w:p>(?:(?!</w:p>).)*\{\{BODY\}\}.*?</w:p>", lambda m: "".join(c.xml), t, flags=re.S)
                if o.lang == "en":
                    t = t.replace('w:val="fr-CA"', 'w:val="en-CA"')
                t = re.sub(r'w:fullDate="[^"]*"', 'w:fullDate="%sT00:00:00Z"' % o.date, t)
            elif info.filename == "word/styles.xml" and o.lang == "en":
                t = t.replace('w:val="fr-CA"', 'w:val="en-CA"')
            elif info.filename == "word/numbering.xml":
                k = t.rindex("</w:num>") + len("</w:num>")  # les <w:num> doivent rester groupés
                t = t[:k] + "".join(c.nums) + t[k:]
            elif info.filename == "word/_rels/document.xml.rels":
                t = t.replace("</Relationships>", "".join(
                    '<Relationship Id="%s" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/image" Target="media/%s"/>'
                    % (rid, nom) for rid, nom, _ in c.images) + "</Relationships>")
            elif info.filename == "word/settings.xml" and "w:updateFields" not in t:
                for balise in ("<w:hdrShapeDefaults", "<w:footnotePr", "<w:endnotePr", "<w:compat"):
                    if balise in t:  # l'ordre des éléments est imposé par le schéma
                        t = t.replace(balise, '<w:updateFields w:val="true"/>' + balise, 1)
                        break
            elif "PublishDate" in t:
                t = re.sub(r"<PublishDate>[^<]*</PublishDate>", "<PublishDate>%sT00:00:00</PublishDate>" % o.date, t)
            data = t.encode("utf-8")
        zout.writestr(info, data)
    for _, nom, chemin in c.images:
        zout.write(chemin, "word/media/" + nom)
    zout.close()
    for av in c.avertissements:
        print("AVERTISSEMENT :", av)
    print("Document créé :", o.sortie)


if __name__ == "__main__":
    main()
