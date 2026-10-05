# Configuration Moniteur LG 65PK640S0UB

**Dernière révision de la section :** 2026-10-05

## Variables

| Variable | Description | Valeur par défaut |
|---|---|---|
| {{IP}} | Adresse IP statique | 192.168.100.22 |
| {{MASQUE}} | Masque | 255.255.255.0 |
| {{PASSERELLE}} | Passerelle | 192.168.100.1 |
| {{VLAN_AV}} | VLAN du réseau AV | 100 |
| {{PORT_COMMUTATEUR}} | Port du commutateur où le moniteur est branché | 8 |
| {{ENTREE}} | Entrée vidéo utilisée | HDMI 1 |
| {{RACCORDEMENT}} | Appareil par lequel le signal arrive (ex. « par l'entremise du récepteur Crestron HD-RXC-4KZ-101 ») | aucune |
| {{ID_MONITEUR}} | « Set ID » du moniteur | 1 |

## Contenu

Le système est équipé d'un moniteur LG 65PK640S0UB raccordé à l'entrée {{ENTREE}} {{RACCORDEMENT}}. Le port réseau du moniteur est branché au port {{PORT_COMMUTATEUR}} du commutateur et le contrôle s'effectue via le réseau. Voici les items couverts dans cette section :

- Configuration réseau.
- Désactivation des modes d'économie d'énergie.
- Configuration pour le contrôle.

## Configuration réseau

Le moniteur devrait recevoir une adresse IP via le DHCP du VLAN {{VLAN_AV}} du commutateur réseau. Pour conserver une constance entre les différentes salles, nous allons assigner l'adresse statique **{{IP}}**. La configuration s'effectue à partir du menu à l'écran du moniteur. Voici les informations à configurer :

| Paramètre | Valeur |
|---|---|
| **Adresse IP** | {{IP}} |
| **Masque** | {{MASQUE}} |
| **Passerelle** | {{PASSERELLE}} |

1. Accéder au menu des réglages du moniteur et ouvrir la section réseau (« **Réseau** » ou « **Network** »).
2. Sélectionner la connexion filaire (Ethernet) et choisir la configuration manuelle de l'adresse.
3. Entrer les paramètres du tableau ci-dessus et confirmer.
4. Valider la communication avec un « ping » vers {{IP}} à partir d'un poste branché sur le VLAN {{VLAN_AV}}.

Le moniteur possède également une interface sans-fil; celle-ci doit être désactivée afin d'éviter deux interfaces actives sur le même réseau.

## Désactivation des modes d'économie d'énergie

Les fonctions d'économie d'énergie doivent être désactivées afin d'éviter que le moniteur s'éteigne de lui-même ou cesse de répondre aux commandes réseau. Ajuster les réglages ci-dessous dans le menu du moniteur :

| Réglage | Valeur |
|---|---|
| Économie d'énergie / « Energy Saving » | Désactivé |
| « Smart Energy Saving » | Désactivé |
| Arrêt automatique après 4 heures | Désactivé |
| Arrêt en absence de signal (15 min) | Désactivé |
| Gestion de l'alimentation (DPM) | Désactivé |
| Mode veille / « PM Mode » | Réglage conservant le réseau actif en veille (« Network Ready ») |
| Wake On LAN | Activé |

Le nom exact des options peut varier selon la version du logiciel webOS installée sur le moniteur. Valider après configuration que le moniteur répond toujours aux commandes réseau lorsqu'il est en veille.

## Configuration pour le contrôle

Le contrôle du moniteur s'effectue par le réseau à partir du processeur, à l'adresse **{{IP}}**. Assigner le « Set ID » **{{ID_MONITEUR}}** au moniteur et activer le contrôle réseau dans le menu. Désactiver la fonction SIMPLINK (HDMI-CEC) afin d'éviter les conflits avec le contrôle du système. Valider que le moniteur retourne sur l'entrée {{ENTREE}} après une coupure d'alimentation.

## Notes

- L'adresse par défaut 192.168.100.22 est aussi celle de la caméra I20 dans les salles de formation.
