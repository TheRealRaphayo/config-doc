# Configuration Projecteur Sharp XP-V731U-W

**Dernière révision de la section :** 2026-10-05

## Variables

| Variable | Description | Valeur par défaut |
|---|---|---|
| {{IP}} | Adresse IP statique | 192.168.100.21 |
| {{MASQUE}} | Masque | 255.255.255.0 |
| {{PASSERELLE}} | Passerelle | 192.168.100.1 |
| {{HOSTNAME}} | Nom d'hôte | PROJ-01 |
| {{VLAN_AV}} | VLAN du réseau AV | 100 |
| {{PORT_COMMUTATEUR}} | Port du commutateur où le projecteur est branché | 7 |
| {{CONTROLEUR}} | Modèle du processeur de contrôle | celui du projet |

## Contenu

Le système est équipé d'un projecteur Sharp XP-V731U-W raccordé par HDBaseT. Le port réseau du projecteur est branché au port {{PORT_COMMUTATEUR}} du commutateur et le contrôle s'effectue via le réseau à partir du processeur {{CONTROLEUR}}. Voici les items couverts dans cette section :

- Configuration réseau.
- Désactivation des modes d'économie d'énergie.
- Configuration pour le contrôle.

## Configuration réseau

Le projecteur devrait recevoir une adresse IP via le DHCP du VLAN {{VLAN_AV}} du commutateur réseau. Pour conserver une constance entre les différentes salles, nous allons assigner l'adresse statique **{{IP}}**. La configuration s'effectue à partir du menu à l'écran du projecteur ou de son interface web. Voici les informations à configurer :

| Paramètre | Valeur |
|---|---|
| **Adresse IP** | {{IP}} |
| **Masque** | {{MASQUE}} |
| **Passerelle** | {{PASSERELLE}} |
| **Nom d'hôte** | {{HOSTNAME}} |

1. Accéder au menu du projecteur et ouvrir la section des paramètres réseau (« **NETWORK SETTINGS** »).
2. Désactiver l'option DHCP et entrer les paramètres du tableau ci-dessus.
3. Appliquer les réglages et redémarrer le projecteur si demandé.
4. Valider la communication avec un « ping » vers {{IP}} à partir d'un poste branché sur le VLAN {{VLAN_AV}}.

## Désactivation des modes d'économie d'énergie

Les fonctions d'économie d'énergie doivent être désactivées afin que le projecteur demeure joignable sur le réseau et qu'il réponde rapidement aux commandes du système de contrôle. Ajuster les réglages ci-dessous dans le menu du projecteur :

| Réglage | Valeur |
|---|---|
| Mode veille (« Standby Mode ») | Réglage permettant de conserver le port LAN actif en veille |
| Arrêt automatique (« Auto Power Off ») | Désactivé |
| Minuterie d'arrêt (« Off Timer ») | Désactivé |
| Mode de la source lumineuse (« Light Mode ») | NORMAL, sauf exigence contraire du client |
| Économiseur d'écran / gestion de l'alimentation | Désactivé |

Sur le XP-V731U, la commande de mise en marche est acceptée par le port LAN peu importe le réglage du mode veille. Il demeure toutefois recommandé de conserver le mode de veille réseau afin d'assurer une réponse rapide et un état fiable rapporté au système de contrôle.

## Configuration pour le contrôle

Le contrôle du projecteur s'effectue par le réseau à partir du processeur, à l'adresse **{{IP}}**. Le projecteur est compatible avec les systèmes de contrôle Crestron et avec PJLink. Si un mot de passe est configuré pour l'accès réseau, celui-ci doit être reporté dans le code et dans le tableau en annexe. Valider que le projecteur sélectionne l'entrée HDBaseT à la mise en marche.

## Notes

- L'adresse par défaut 192.168.100.21 est aussi celle de la caméra I12 dans les salles de formation.
