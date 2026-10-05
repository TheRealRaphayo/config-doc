# config-doc — skill de génération de documents de configuration

Skill pour Claude : à partir d'une liste d'équipements, il assemble un document
de configuration en combinant les sections propres à chaque équipement.

## Structure

```
SKILL.md                      procédure suivie par Claude
references/index.md           table équipement → fichier de section
references/_modele-section.md modèle à copier pour un nouvel équipement
references/*.md               une section par équipement, programme ou procédure
assets/images/                captures d'écran utilisées par les sections
assets/gabarit.docx           mise en page Word (page titre, en-têtes, styles)
scripts/assembler_docx.py     insère le contenu assemblé dans le gabarit
exemples/                     exemple de liste d'équipements
```

## Ajouter un équipement

1. Copier `references/_modele-section.md` sous le nom `fabricant-modele.md`.
2. Remplir les étapes. Remplacer toute valeur propre à un projet par une variable `{{NOM}}`
   et la déclarer dans le tableau « Variables », avec sa valeur par défaut s'il y en a une.
3. Ajouter une ligne dans `references/index.md` (avec les autres noms du modèle).
4. Ouvrir une merge/pull request pour révision.

## Règles du dépôt

- **Aucun mot de passe ni donnée de client** dans les sections et les images : pas
  de noms de client, de projet ou de site. Ces valeurs viennent de la liste
  d'équipements à la génération. Les adresses standards de vos salles
  (192.168.100.x) sont permises comme valeurs par défaut.
- Une section = un fichier. Corriger une procédure se fait dans son fichier seulement.
- Noter la version de micrologiciel validée en tête de chaque section.

## Installer ou mettre à jour le skill dans Claude

Le skill ne se synchronise pas automatiquement avec le dépôt.

1. Créer une archive zip dont la racine est un dossier `config-doc/` contenant
   `SKILL.md` et les sous-dossiers.
2. La téléverser dans Claude (Paramètres → section des skills).
3. Refaire ces étapes après chaque changement fusionné. Un tag Git par version
   installée permet de savoir quelle version a produit un document donné.

## Utilisation

Fournir à Claude la liste d'équipements (CSV, Excel ou texte) et demander le
document de configuration, en précisant le client et le projet.
