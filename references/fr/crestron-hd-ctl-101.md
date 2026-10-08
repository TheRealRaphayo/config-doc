# Configuration HD-CTL-101

**Dernière révision de la section :** 2026-10-03

## Variables

| Variable | Description | Valeur par défaut |
|---|---|---|
| {{CONTROLLER_IP}} | Adresse IP du contrôleur | celle du contrôleur du projet |
| {{USERNAME}} / {{PASSWORD}} | Compte administrateur | aucune |
| {{AV_VLAN}} | VLAN du réseau AV | 100 |

Valeurs par défaut par unité :

| Unité | IP-ID | Adresse IP | Masque | « Default Router » |
|---|---|---|---|---|
| Moniteur Droit | 5 | 192.168.100.5 | 255.255.255.0 | 192.168.100.1 |
| Moniteur Côté | 6 | 192.168.100.6 | 255.255.255.0 | 192.168.100.1 |

## Contenu

Le système est équipé de HD-CTL-101 pour les salles multifonctionnelles. Ces interfaces permettent le contrôle des moniteurs. Voici les items couverts dans cette section :

- Configuration réseau et table IP

Lors du démarrage initial de l'interface, il est demandé d'entrer un mot de passe par défaut. Voici l'usager et le mot de passe qui ont été configurés.

**{{USERNAME}} / {{PASSWORD}}**

## Configuration réseau et table IP

Les interfaces devraient recevoir une adresse IP via le DHCP du VLAN {{AV_VLAN}} du commutateur réseau. Pour conserver une constance entre les différentes salles, nous allons assigner une adresse statique à chacune des interfaces et un IP-ID. Assurez-vous d'utiliser l'adresse IP du contrôleur **{{CONTROLLER_IP}}** pour permettre la communication. Vous pouvez effectuer cette opération en vous branchant via le fureteur internet. Voici les informations à configurer :

{{UNIT_TABLE : Interface, IP-ID, Adresse IP, Masque, « Default Router »}}
