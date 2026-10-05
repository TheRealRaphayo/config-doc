---
name: config-doc
description: Génère un document de configuration AV à partir d'une liste d'équipements, en assemblant les sections de configuration propres à chaque équipement (Crestron, QSC, Sennheiser, Netgear, etc.) dans un gabarit commun. À utiliser dès que l'utilisateur fournit une liste d'équipements, un bordereau ou un BOM et demande un document, guide ou cahier de configuration, de mise en service ou de programmation, même s'il ne nomme pas ce skill. Also triggers on English requests such as "build the configuration document from this equipment list".
---

# Document de configuration à partir d'une liste d'équipements

Ce skill assemble un document de configuration en choisissant, dans `references/`,
les sections qui correspondent aux équipements de la liste fournie.

Le contenu technique vient uniquement des fichiers de section. Un technicien va
suivre ce document sur le terrain : une étape inventée peut lui faire perdre des
heures ou mal configurer un appareil. Quand une information manque, le document
doit le montrer clairement plutôt que la combler par une supposition.

## Procédure

### 1. Lire la liste d'équipements

La liste arrive en CSV, Excel ou collée dans la conversation, **une ligne par
unité** (voir `exemples/liste-equipements.csv`) :

| Colonne | Obligatoire | Contenu |
|---|---|---|
| fabricant | oui | ex. Crestron |
| modele | oui | ex. RMC4 |
| description | non | rôle ou nom de l'unité (ex. « DEC-01 », « Moniteur Droit ») |
| ip_id | non | IP-ID Crestron |
| ip, masque, passerelle | non | adresse statique, ou « DHCP » |
| hostname | non | nom d'hôte |
| utilisateur, mot_de_passe | non | compte de l'appareil |
| notes | non | particularités du projet |

Si les colonnes portent d'autres noms mais que le sens est clair, les associer
sans redemander. Si fabricant ou modèle manque, le demander à l'utilisateur.
Une colonne `quantite` est acceptée : la ligne compte alors pour autant d'unités.

Relever aussi ce que l'utilisateur donne dans la conversation : client, projet,
salle, auteur, programme installé, noms des fichiers de programme et d'interface.
La langue du document est le français, sauf demande contraire.

### 2. Associer chaque équipement à sa section

Lire `references/index.md`. Pour chaque modèle de la liste, trouver le fichier de
section (l'index donne aussi les autres noms d'un même modèle).

- Section trouvée : lire ce fichier, et seulement ceux qui sont nécessaires.
- Aucune section : ne rien rédiger pour cet équipement. Il apparaît dans l'annexe
  et dans la liste des équipements sans section (étape 6).
- Modèle ambigu : demander à l'utilisateur.

Vérifier ensuite les deux autres tableaux de l'index :

- **Sections conditionnelles** : les inclure quand leur condition est remplie.
- **Programmes** : inclure le fichier du programme installé. Si l'utilisateur ne
  l'a pas indiqué, le lui demander ; s'il n'y en a pas, omettre ces parties.

### 3. Résoudre les variables

Les sections contiennent des variables `{{NOM}}`. Chaque section les déclare dans
son tableau « Variables », avec une valeur par défaut quand il y en a une.
Ordre de priorité pour chaque variable :

1. la valeur de la liste d'équipements ou de la conversation ;
2. la valeur par défaut déclarée dans la section ;
3. sinon, la variable reste visible sous la forme **[À COMPLÉTER : NOM]** et est
   reportée à l'étape 6.

Variables calculées :

- `{{IP_CONTROLEUR}}` : adresse IP du processeur de contrôle du projet.
- `{{QUANTITE}}` : nombre d'unités de ce modèle dans la liste.
- `{{TABLEAU_UNITES : colonnes}}` : remplacer par un tableau des unités de ce
  modèle, une colonne par unité comme dans les documents d'origine (ou une ligne
  par unité s'il y en a plus de quatre). Prendre les valeurs de la liste, puis
  les « Valeurs par défaut par unité » de la section s'il y en a.

Si une valeur de la liste contredit une valeur par défaut, la liste l'emporte.
Si deux unités de la liste ont la même adresse IP ou le même IP-ID, le signaler
à l'utilisateur avant de produire le document.

Ne pas inclure dans le document les tableaux « Variables » et « Valeurs par
défaut par unité », les lignes « Dernière révision », ni les sections « Notes »
des fichiers : ils servent à l'entretien du dépôt.

### 4. Assembler le document

Ordre du document, calqué sur les documents d'origine :

1. Page titre (client, projet, salle) et table des matières
2. **Information du système** : partie du même nom dans le fichier du programme
3. **Configuration matérielle** : une section par modèle d'équipement, dans
   l'ordre de l'index, avec les sections conditionnelles à l'emplacement indiqué
4. **Configuration logiciel** : partie du même nom dans le fichier du programme
5. **Annexe** : tableau de toutes les unités de la liste, avec les colonnes
   Manufacturier, Équipement, Description, ID, Adresse, Masque, Passerelle,
   Utilisateur, Mot de passe
6. **Éléments à compléter** (seulement s'il y en a)

Règles d'assemblage :

- **Niveaux de titre.** Dans les fichiers, `#` est le titre de l'équipement.
  Décaler les niveaux pour que chaque équipement soit une sous-section de
  « Configuration matérielle ». La partie « Contenu » d'un fichier devient
  l'introduction de la section, sans son titre.
- **Plusieurs unités du même modèle.** La procédure n'apparaît qu'une fois.
- **Blocs optionnels.** Un bloc entre `<!-- SI: condition -->` et `<!-- FIN SI -->`
  est gardé seulement si la condition est vraie pour ce projet. Dans le doute,
  demander à l'utilisateur.
- **Consignes.** Un commentaire `<!-- CONSIGNE : ... -->` dit comment adapter le
  tableau ou le paragraphe qui le suit au projet. L'appliquer, sans le recopier.
- **Images.** Les sections référencent des captures dans `assets/images/`. Les
  insérer à l'endroit indiqué. Un commentaire `<!-- IMAGE À FOURNIR : ... -->`
  n'a pas d'image : ne rien insérer.
- **Fidélité.** Reprendre les étapes telles qu'écrites. Ne pas reformuler les
  valeurs, noms de menus ou commandes.

### 5. Produire le fichier

Le gabarit `assets/gabarit.docx` fournit la page titre, les en-têtes, les pieds de
page et les styles. Le script `scripts/assembler_docx.py` y insère le contenu :

1. Écrire le contenu assemblé (étapes 2 à 4, à partir de « Information du
   système ») dans un fichier `corps.md`, en Markdown simple : titres `#` à `###`,
   paragraphes, `**gras**`, listes `- ` et `1. `, tableaux à barres verticales,
   images `![texte](../assets/images/nom.png)`. Ne pas y mettre la page titre ni
   la table des matières : le gabarit les contient.
2. Lancer le script depuis le dossier du skill :

   ```bash
   python scripts/assembler_docx.py corps.md --client "<client>" --salle "<salle>" \
       --type-salle "<type de salle>" --revision 1.0 --sortie <fichier>.docx
   ```

   `--type-salle` est le texte de l'en-tête après le nom du client. `--date`
   (AAAA-MM-JJ) est optionnel ; par défaut, la date du jour.
3. Le script refuse un corps qui contient encore des `{{VARIABLES}}` : les
   remplacer par leur valeur ou par `[À COMPLÉTER : NOM]` (surligné en jaune dans
   le document), puis relancer.
4. Convertir le résultat en PDF et regarder quelques pages pour vérifier la mise
   en page avant de le remettre (voir le skill `docx` de l'environnement).

La table des matières se met à jour à l'ouverture dans Word, qui demande alors
de confirmer la mise à jour des champs : le mentionner à l'utilisateur.

Si l'utilisateur demande un autre format (PDF, Markdown), produire d'abord le
Word, puis le convertir.

Nom du fichier : `<client>_<salle>_Configuration` (sans accents ni espaces).

### 6. Signaler ce qui manque

La partie « Éléments à compléter » du document regroupe :

- les équipements de la liste qui n'ont pas de section dans `references/` ;
- les variables restées sans valeur, par équipement.

Répéter ces deux points dans la réponse à l'utilisateur, en quelques lignes, pour
qu'il sache quoi fournir ou quelle section ajouter au dépôt. Rappeler aussi, si
le document contient des mots de passe, qu'il doit être diffusé en conséquence.

## Ajouter ou modifier une section

Voir `README.md` à la racine. Le modèle de section est `references/_modele-section.md`.
