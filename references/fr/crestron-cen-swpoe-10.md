# Commutateur réseau

**Dernière révision de la section :** 2026-10-05

## Variables

| Variable | Description | Valeur par défaut |
|---|---|---|
| {{IP}} | Adresse IP statique du commutateur (passerelle du VLAN AV) | 192.168.100.1 |
| {{SUBNET_MASK}} | Masque | 255.255.255.0 |
| {{HOSTNAME}} | Nom d'hôte | SW-01 |
| {{AV_VLAN}} | VLAN du réseau AV | 100 |
| {{CONTROLLER}} | Modèle du contrôleur alimenté en PoE | celui du projet |

## Contenu

Le système est équipé d'un commutateur réseau Crestron CEN-SWPOE-10. Il s'agit d'un commutateur géré de dix ports dont huit offrent le PoE+ (802.3at, jusqu'à 30 W par port) en plus de deux ports SFP+. Celui-ci est configuré en mode indépendant pour la communication du système AV et alimente le clavier {{CONTROLLER}}. Voici la liste des items couverts dans cette section :

- Configuration réseau du commutateur.
- Configuration des ports et du PoE.
- Sauvegarde de la configuration.

## Configuration réseau du commutateur

Le commutateur agit comme passerelle du VLAN AV {{AV_VLAN}}. Pour conserver une constance entre les différentes salles, nous allons lui assigner l'adresse statique **{{IP}}**. Par défaut, le commutateur obtient son adresse par DHCP ou utilise l'adresse 169.254.100.100 s'il n'y a pas de DHCP; la configuration s'effectue ensuite via son interface web.

1. Brancher un poste de travail sur un port du commutateur et repérer l'adresse obtenue par DHCP.
2. Ouvrir un fureteur web et entrer l'adresse du commutateur.
3. Vous connecter avec l'usager et le mot de passe configurés (voir le tableau en annexe).
4. Dans la section de configuration réseau, sélectionner l'adressage statique et entrer les paramètres ci-dessous :

| Paramètre | Valeur |
|---|---|
| **Adresse IP** | {{IP}} |
| **Masque** | {{SUBNET_MASK}} |
| **Nom d'hôte** | {{HOSTNAME}} |

5. Appliquer et sauvegarder la configuration; le commutateur sera ensuite accessible à l'adresse {{IP}}.

## Configuration des ports et du PoE

Tous les appareils AV de la salle sont raccordés sur le VLAN {{AV_VLAN}}. Assurez-vous que le PoE est activé sur le port du clavier {{CONTROLLER}}, celui-ci n'ayant aucune autre source d'alimentation. Voici l'assignation des ports :

<!-- INSTRUCTION: le tableau ci-dessous est l'assignation de la salle de présentation standard. Retirer les lignes des équipements absents de la liste. Si l'utilisateur fournit une autre assignation, l'utiliser. Si la liste contient des équipements réseau qui ne sont pas dans ce tableau, demander leur port à l'utilisateur. -->

| Port | Appareil |
|---|---|
| 1 | Crestron HD-PS402 |
| 2 | Crestron MPC4-102-B (PoE+ requis) |
| 3 à 6 | Réserve – périphériques AV additionnels |
| 7 | Sharp XP-V731U-W |
| 8 | LG 65PK640S0UB |
| 9 et 10 (SFP+) | Liaison montante vers le réseau corporatif, si requise |

## Sauvegarde de la configuration

Lorsque la configuration est complétée, exporter le fichier de configuration du commutateur et le conserver avec la documentation de la salle. Ce fichier pourra être réimporté lors du remplacement de l'équipement.
