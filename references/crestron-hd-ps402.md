# Configuration Système de présentation HD-PS402

**Version du micrologiciel de référence :** hd-ps401_hd-ps402_hd-ps621_hd-ps622_1.4.4790.00075.puf
**Dernière révision de la section :** 2026-10-05

## Variables

| Variable | Description | Valeur par défaut |
|---|---|---|
| {{IP}} | Adresse IP statique | 192.168.100.10 |
| {{MASQUE}} | Masque | 255.255.255.0 |
| {{PASSERELLE}} | « Default Router » | 192.168.100.1 |
| {{UTILISATEUR}} / {{MOT_DE_PASSE}} | Compte administrateur | aucune |
| {{VLAN_AV}} | VLAN du réseau AV | 100 |
| {{FICHIER_MICROGICIEL}} | Fichier de micrologiciel installé | aucune |
| {{CONTROLEUR}} | Modèle du processeur de contrôle | celui du projet |
| {{IP_CONTROLEUR}} | Adresse IP du processeur de contrôle | celle du contrôleur du projet |
| {{AMPLIFICATEUR}} | Modèle de l'amplificateur alimenté par la sortie AUX | celui du projet |

## Contenu

Le système est équipé d'un système de présentation Crestron HD-PS402 offrant quatre entrées HDMI et deux sorties HDMI avec sorties DM Lite miroir. Celui-ci effectue la commutation automatique des sources, la mise à l'échelle vers le moniteur, la gestion de l'EDID ainsi que le mixage et la séparation de l'audio. Voici les items couverts dans cette section :

- Configuration réseau.
- Mise à jour du micrologiciel.
- Configuration de la commutation automatique et de l'EDID.
- Configuration audio.
- Configuration de la table IP.

Lors du démarrage initial de l'appareil, il est demandé d'entrer un mot de passe par défaut. Voici l'usager et le mot de passe qui ont été configurés.

**{{UTILISATEUR}} / {{MOT_DE_PASSE}}**

## Configuration réseau

L'appareil devrait recevoir une adresse IP via le DHCP du VLAN {{VLAN_AV}} du commutateur réseau. Pour conserver une constance entre les différentes salles, nous allons assigner l'adresse statique **{{IP}}**. Vous pouvez effectuer cette opération via l'interface web de l'appareil ou avec Crestron Toolbox. Voici les informations à configurer :

| Paramètre | Valeur |
|---|---|
| **Adresse IP** | {{IP}} |
| **Masque** | {{MASQUE}} |
| **« Default Router »** | {{PASSERELLE}} |

## Mise à jour du micrologiciel

Procéder à la mise à jour du HD-PS402 avec la version la plus récente disponible sur le site de Crestron, à partir de l'option « **Update Firmware** » de l'interface web de l'appareil.

**{{FICHIER_MICROGICIEL}}**

## Configuration de la commutation automatique et de l'EDID

La commutation automatique et la gestion de l'EDID se configurent à partir de l'interface web du HD-PS402. Suivre les étapes ci-dessous :

1. Dans la section des entrées, activer la commutation automatique et choisir le mode désiré, soit la dernière entrée branchée ou la priorité assignée à chacune des entrées.
2. Assigner la priorité de chacune des entrées selon l'usage de la salle.
3. Valider que l'entrée raccordée à la plaque murale est incluse dans la commutation automatique.
4. Dans la section EDID, assigner un EDID correspondant à la capacité du moniteur installé.
5. Sauvegarder la configuration.

## Configuration audio

<!-- SI: un amplificateur est raccordé à la sortie AUX -->
Le HD-PS402 sépare l'audio de la source sélectionnée et l'achemine vers la sortie AUX qui alimente l'amplificateur {{AMPLIFICATEUR}}. Ajuster le mixeur de la sortie utilisée, régler le niveau de sortie et valider que le mode de raccordement, balancé ou non balancé, correspond au câblage vers l'amplificateur. La plage d'ajustement du volume utilisée par le code doit également être validée afin d'éviter l'écrêtage.
<!-- FIN SI -->

## Configuration de la table IP

Configurer la table IP du HD-PS402 pour communiquer avec le processeur {{CONTROLEUR}} à l'adresse **{{IP_CONTROLEUR}}**. Consulter le tableau en annexe pour l'IP-ID à utiliser. Vous pouvez assigner le ID via Crestron Toolbox ou via l'interface web de l'appareil.

## Notes

- Le document d'origine utilisait l'IP-ID 05 et ajoutait que le HD-PS402 « héberge la configuration de l'émetteur HD-TX-4KZ-211-2G » ; cette phrase a été retirée du texte générique, à remettre si elle s'applique à toutes les salles.
- L'adresse par défaut 192.168.100.10 est aussi celle du QSC Core dans les salles de formation.
