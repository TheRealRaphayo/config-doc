# Commutateur réseau

**Logiciel de référence :** Netgear Engage
**Dernière révision de la section :** 2026-10-03

## Variables

| Variable | Description | Valeur par défaut |
|---|---|---|
| {{MODEL}} | Modèle du commutateur | M4250-8G2XF-PoE+ (GSM4210PX) |
| {{NETGEAR_SITE}} | Nom du modèle de site Netgear Engage | aucune |
| {{SITE_PASSWORD}} | Mot de passe de configuration du site | aucune |
| {{AV_VLAN}} | VLAN du réseau AV | 100 |

## Contenu

Le système est équipé d'un commutateur réseau Netgear {{MODEL}}. Celui-ci est configuré en mode indépendant pour la communication du système AV. Un fichier de configuration est disponible pour téléverser dans celui-ci. Voici la liste des items couverts dans cette section :

- Netgear Engage - Importation du site.
- Netgear Engage - Assigner commutateur au site.

## Netgear Engage - Importation du site

En utilisant le logiciel Netgear Engage, importer le modèle de site {{NETGEAR_SITE}}. Si votre logiciel Netgear Engage dispose déjà de ce site, vous pouvez ignorer cette étape.

1. Ouvrir Netgear Engage.
2. Aller dans la section « Controller Management ».
3. Sélectionner l'option « Import Site ».
4. Choisir le site « {{NETGEAR_SITE}}_yyyy-mm-dd_hh-mm-ss_x.zip ».
5. Entrer le mot de passe de configuration « {{SITE_PASSWORD}} ».
6. Appuyer sur « Upload ».

<!-- IF: le commutateur doit être assigné au site dans Netgear Engage -->
## Netgear Engage - Assigner commutateur au site

Lorsque le site a été ajouté à votre logiciel Netgear Engage, vous pouvez l'utiliser sur le commutateur. Assurez-vous de sélectionner la bonne interface réseau. Suivre les étapes ci-dessous :

1. Dans le menu « Devices », sélectionner le site dans le menu déroulant.
2. Dans le menu « Discovered Devices », cliquer sur « Onboard » pour ajouter le commutateur.

Lorsque le commutateur a été assigné, il devrait être configuré pour le modèle de configuration de ce type de salle. Les ports 1 à 3 et 5 à 8 sont assignés sur le VLAN AV {{AV_VLAN}}. Les ports 4, 9 et 10 restent sur le VLAN « Management » 1.

<!-- IMAGE NEEDED: vue des ports du commutateur dans Netgear Engage (capture d'origine retirée : elle affichait le nom du site du client) -->
<!-- END IF -->
