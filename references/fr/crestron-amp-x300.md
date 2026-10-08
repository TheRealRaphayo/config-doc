# Configuration Amplificateur AMP-X300

**Dernière révision de la section :** 2026-10-05

## Variables

| Variable | Description | Valeur par défaut |
|---|---|---|
| {{AUDIO_SOURCE}} | Appareil qui alimente l'amplificateur | celui du projet (ex. HD-PS402) |

## Contenu

Le système est équipé d'un amplificateur Crestron AMP-X300, un amplificateur quatre canaux d'une puissance totale de 300 W. Celui-ci ne possède aucune interface réseau; toute la configuration se fait à partir des commandes en façade et du câblage. Voici les items couverts dans cette section :

- Sélection du mode de sortie.
- Ajustement des gains.
- Mode veille.

## Sélection du mode de sortie

Les interrupteurs en façade permettent de configurer les paires de canaux en basse impédance (4 ou 8 ohms), en mode ponté ou en haute impédance (70 V / 100 V). Sélectionner le mode correspondant aux haut-parleurs installés **avant** de mettre l'amplificateur sous tension, puis valider le câblage des sorties.

## Ajustement des gains

Chaque canal dispose d'un ajustement de gain indépendant. Régler d'abord le niveau de sortie du {{AUDIO_SOURCE}}, puis ajuster les gains de l'amplificateur afin d'obtenir le niveau désiré dans la salle sans écrêtage. Noter les positions retenues dans la documentation de la salle.

## Mode veille

L'entrée **REMOTE** accepte un contact sec permettant de placer les sorties en veille. Si cette fonction est utilisée, la raccorder à un relais du système de contrôle. Autrement, l'amplificateur passe automatiquement en veille après une période sans signal et se réactive dès qu'un signal est détecté.
