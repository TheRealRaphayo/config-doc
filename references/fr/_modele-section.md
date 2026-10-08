> **MODÈLE DE SECTION** — copier ce fichier, le renommer `fabricant-modele.md`
> (minuscules, tirets), l'ajouter à `index.md`, puis supprimer cet encadré.
> Créer aussi la version anglaise dans `en/`, sous le même nom de fichier.
>
> - Les variables et les marqueurs s'écrivent en anglais dans les deux langues.
>
> - Aucun mot de passe, nom de client ou nom de projet : en faire des variables `{{NAME}}`.
> - Les adresses standards de vos salles peuvent servir de valeurs par défaut.
> - Variables fournies par la liste d'équipements :
>   `{{IP}}` `{{SUBNET_MASK}}` `{{GATEWAY}}` `{{HOSTNAME}}` `{{IP_ID}}`
>   `{{USERNAME}}` `{{PASSWORD}}` `{{QUANTITY}}`
> - Variables calculées : `{{CONTROLLER_IP}}`, `{{UNIT_TABLE : colonnes}}`.
> - Bloc optionnel : l'encadrer par `<!-- IF: condition en clair -->` et `<!-- END IF -->`.
> - Contenu à adapter au projet (ex. assignation des ports) : le faire précéder de
>   `<!-- INSTRUCTION: quoi adapter et comment -->`.
> - Image : la déposer dans `assets/images/` sous le nom `fabricant-modele_sujet.png`
>   et vérifier qu'elle ne montre ni mot de passe ni information de client.

# Configuration Fabricant Modèle

**Version du micrologiciel de référence :** (version validée pour cette procédure)
**Dernière révision de la section :** AAAA-MM-JJ

## Variables

| Variable | Description | Valeur par défaut |
|---|---|---|
| {{IP}} | Adresse IP statique | (adresse standard, ou « aucune ») |
| {{USERNAME}} / {{PASSWORD}} | Compte administrateur | aucune |

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

![Description de la capture](../../assets/images/fabricant-modele_sujet.png)

<!-- IF: condition en clair -->
## Sous-section optionnelle

1. (étape)
<!-- END IF -->

## Notes

- (remarques pour l'entretien de la section ; non reprises dans le document)
