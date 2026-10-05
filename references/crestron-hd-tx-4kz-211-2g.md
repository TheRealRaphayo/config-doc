# Configuration Émetteur HD-TX-4KZ-211-2G

**Dernière révision de la section :** 2026-10-05

## Variables

| Variable | Description | Valeur par défaut |
|---|---|---|
| {{EMPLACEMENT}} | Emplacement de la plaque | au mur |
| {{RECEPTEUR}} | Appareil qui reçoit le lien DM Lite de l'émetteur | aucune |

## Contenu

Le système est équipé d'une plaque murale émettrice Crestron HD-TX-4KZ-211-2G installée {{EMPLACEMENT}}. Celle-ci offre une entrée HDMI et une entrée USB-C (DisplayPort Alt Mode) avec commutation automatique 2x1, et achemine le signal vers l'entrée DM Lite du {{RECEPTEUR}} par un câble CAT5e ou supérieur. L'émetteur ne possède pas d'adresse IP. Voici les items couverts dans cette section :

- Alimentation.
- Vérification du lien DM Lite.
- Commutation automatique.

## Alimentation

[À COMPLÉTER : mode d'alimentation de l'émetteur]

Le voyant **PWR** est ambre pendant le démarrage et vert lorsque l'appareil est fonctionnel.

## Vérification du lien DM Lite

Le voyant **LINK** doit être vert, ce qui confirme que le lien DM Lite est établi avec le {{RECEPTEUR}}. Valider également que le voyant de l'entrée utilisée est vert, ce qui indique que la source est détectée et acheminée vers la sortie.

## Commutation automatique

Le bouton **AUTO** en façade active ou désactive la commutation automatique entre l'entrée HDMI et l'entrée USB-C; le voyant AUTO est vert lorsque la fonction est activée.

## Notes

- Le document d'origine se contredit sur deux points, à trancher avant de fixer le texte :
  - Alimentation : « Le HD-TX-4KZ-211-2G est alimenté par le HD-RXC-4KZ-101. Un bloc d'alimentation 24 V (vendu séparément) doit donc être raccordé à la borne 24V 0.7A de l'émetteur. » Soit l'émetteur est alimenté par le lien, soit par un bloc local.
  - Lien DM Lite : l'introduction dit que le signal va vers le HD-RXC-4KZ-101, la vérification du lien dit qu'il est établi avec le HD-PS402.
