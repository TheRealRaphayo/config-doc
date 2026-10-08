# Configuration UC-Engine

**Dernière révision de la section :** 2026-10-03

## Variables

| Variable | Description | Valeur par défaut |
|---|---|---|
| {{IP}} | Adresse IP de l'adaptateur réseau de contrôle | 192.168.100.3 |
| {{SUBNET_MASK}} | Masque | 255.255.255.0 |
| {{GATEWAY}} | « Default Router » | 192.168.100.1 |
| {{IP_ID}} | IP-ID dans la table IP | 3 |
| {{AUDIO_DEVICE}} | Périphérique audio à sélectionner (ex. QSC Core) | aucune |
| {{CAMERA}} | Caméra à sélectionner | Crestron 1 Beyond i12 |
| {{UI_FILE}} | Fichier de l'interface de contrôle (.ch5z) | aucune |

## Contenu

Le système est équipé d'un ordinateur Teams Crestron UC-Engine pour permettre aux usagers de placer et recevoir des appels. Voici les items couverts dans cette section :

- Configuration communication entre les appareils.
- Configuration table IP.
- Configuration des périphériques audio et vidéo.
- Implantation de l'interface de contrôle.

## Configuration communication entre les appareils

Configurer l'adaptateur réseau dédié à la communication avec le processeur en utilisant les informations ci-dessous :

| Paramètre | Valeur |
|---|---|
| **Adresse IP** | {{IP}} |
| **Masque** | {{SUBNET_MASK}} |
| **« Default Router »** | {{GATEWAY}} |

Il est recommandé de renommer l'adaptateur réseau en utilisant « Crestron Control ».

![Adaptateur réseau](../../assets/images/crestron-uc-engine_adaptateur-reseau.png)

## Configuration Table IP

Configurer la table IP du UC-Engine pour communiquer avec le processeur (IP-ID {{IP_ID}}). Consulter le tableau en annexe pour plus d'information. Vous pouvez assigner le ID via Crestron Toolbox ou en utilisant l'application Crestron Settings en mode administrateur.

## Configuration des périphériques audio et vidéo

Assurez-vous de sélectionner les périphériques audio {{AUDIO_DEVICE}} ainsi que la caméra {{CAMERA}} dans le UC-Engine.

![Périphériques](../../assets/images/crestron-uc-engine_peripheriques.png)

## Implantation de l'interface de contrôle

La procédure ci-dessous explique la démarche à utiliser pour implanter l'interface de contrôle. Il est important d'implanter les fichiers de configuration avant d'implanter le code.

1. Utiliser l'option « **Text Console** » dans le logiciel Crestron Toolbox et vous brancher au UC-Engine via réseau.
2. Lorsque branché, utiliser l'option « **Project** » dans le logiciel Crestron Toolbox.
3. Appuyer sur le bouton « **Browse** », choisir le fichier **{{UI_FILE}}** et sélectionner « **Open** ».
4. Appuyer sur le bouton « **Send** » pour téléverser le panneau vers le UC-Engine.
