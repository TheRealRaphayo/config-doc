# Gabarit et images

## gabarit.docx

Mise en page Word : page titre, en-têtes, pieds de page, page de droits d'auteur
et styles. Le script `scripts/assembler_docx.py` y remplace ces champs :

| Champ | Où | Source |
|---|---|---|
| `{{CLIENT}}` | page titre, en-têtes, propriétés | `--client` |
| `{{ROOM}}` | page titre, en-tête de la page titre | `--salle` |
| `{{ROOM_TYPE}}` | en-tête des pages | `--type-salle` |
| `{{REVISION}}` | bandeau de la page titre | `--revision` |
| `{{DATE}}` | bandeau de la page titre | `--date` |
| `{{BODY}}` | après la page de droits d'auteur | fichier `corps.md` |
| `{{TOC_TITLE}}` | titre de la table des matières | `--lang` (« Contenus » ou « Contents ») |
| `{{TOC_HINT}}` | texte provisoire de la table des matières | `--lang` |

Pour modifier la mise en page, ouvrir `gabarit.docx` dans Word et conserver ces
champs tels quels. Le script utilise les styles Titre 1 à 3, Paragraphe de liste
et Grille du tableau : ne pas les supprimer ni les renommer.

## images/

Captures d'écran référencées par les sections, nommées `fabricant-modele_sujet.png`.
Avant d'en ajouter une, vérifier qu'elle ne montre ni mot de passe, ni nom de
client, ni vue d'une salle de client.
