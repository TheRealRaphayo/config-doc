> **MODÈLE DE SECTION** — copier ce fichier, le renommer `fabricant-modele.md`
> (minuscules, tirets), l'ajouter à `index.md`, puis supprimer cet encadré.
>
> - Aucun mot de passe, nom de client ou nom de projet : en faire des variables `{{NOM}}`.
> - Les adresses standards de vos salles peuvent servir de valeurs par défaut.
> - Variables fournies par la liste d'équipements :
>   `{{IP}}` `{{MASQUE}}` `{{PASSERELLE}}` `{{HOSTNAME}}` `{{IP_ID}}`
>   `{{UTILISATEUR}}` `{{MOT_DE_PASSE}}` `{{QUANTITE}}`
> - Variables calculées : `{{IP_CONTROLEUR}}`, `{{TABLEAU_UNITES : colonnes}}`.
> - Bloc optionnel : l'encadrer par `<!-- SI: condition en clair -->` et `<!-- FIN SI -->`.
> - Image : la déposer dans `assets/images/` sous le nom `fabricant-modele_sujet.png`
>   et vérifier qu'elle ne montre ni mot de passe ni information de client.

# Configuration Fabricant Modèle

**Version du micrologiciel de référence :** (version validée pour cette procédure)
**Dernière révision de la section :** AAAA-MM-JJ

## Variables

| Variable | Description | Valeur par défaut |
|---|---|---|
| {{IP}} | Adresse IP statique | (adresse standard, ou « aucune ») |
| {{UTILISATEUR}} / {{MOT_DE_PASSE}} | Compte administrateur | aucune |

## Contenu

(Une ou deux phrases : rôle de l'équipement dans le système.) Voici les items couverts dans cette section :

- (sous-section)
- (sous-section)

## Configuration réseau

1. (étape)
2. (étape)

| Paramètre | Valeur |
|---|---|
| **Adresse IP** | {{IP}} |

![Description de la capture](../assets/images/fabricant-modele_sujet.png)

<!-- SI: condition en clair -->
## Sous-section optionnelle

1. (étape)
<!-- FIN SI -->

## Notes

- (remarques pour l'entretien de la section ; non reprises dans le document)
