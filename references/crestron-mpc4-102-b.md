# Configuration Contrôleur Crestron MPC4-102-B

**Version du micrologiciel de référence :** mpc4-mpb4_2.8006.00322.01.puf
**Dernière révision de la section :** 2026-10-05

## Variables

| Variable | Description | Valeur par défaut |
|---|---|---|
| {{IP}} | Adresse IP statique du contrôleur | 192.168.100.2 |
| {{MASQUE}} | Masque | 255.255.255.0 |
| {{PASSERELLE}} | « Default Router » | 192.168.100.1 |
| {{HOSTNAME}} | Nom d'hôte | MPC-01 |
| {{UTILISATEUR}} / {{MOT_DE_PASSE}} | Compte administrateur | aucune |
| {{VLAN_AV}} | VLAN du réseau AV | 100 |
| {{FICHIER_MICROGICIEL}} | Fichier de micrologiciel installé | aucune |
| {{FICHIER_PROGRAMME}} | Fichier du programme (.lpz) | aucune |

## Contenu

Voici les items couverts dans cette section.

- Configuration réseau.
- Configuration d'authentification.
- Configuration horloge du système.
- Mise à jour du micrologiciel.
- Configuration de l'interface usager.
- Implantation du code.

Lors du démarrage initial du processeur, il est demandé d'entrer un mot de passe par défaut. Voici l'usager et le mot de passe qui ont été configurés.

**{{UTILISATEUR}} / {{MOT_DE_PASSE}}**

## Configuration réseau

Le processeur devrait recevoir une adresse IP via le DHCP du VLAN {{VLAN_AV}} du commutateur réseau. Pour conserver une constance entre les différentes salles, nous allons assigner l'adresse statique **{{IP}}**. Vous pouvez effectuer cette opération en utilisant Crestron Toolbox.

1. Utiliser l'option « **Text Console** » dans le logiciel Crestron Toolbox et vous brancher au MPC4-102-B via réseau ou USB.
2. Lorsque branché, utiliser l'option « **Ethernet Addressing** » dans le menu « **Functions** ».
3. Cocher l'option « **IP Static** » et entrer les paramètres ci-dessous :

| Paramètre | Valeur |
|---|---|
| **Adresse IP** | {{IP}} |
| **Masque** | {{MASQUE}} |
| **« Default Router »** | {{PASSERELLE}} |
| **Nom d'hôte** | {{HOSTNAME}} |

4. Lorsque complété, appuyer sur « **Apply** » et le processeur va redémarrer.

## Configuration d'authentification

Il est conseillé de procéder à la configuration des options d'authentification. Vous pouvez y ajouter des usagers, des groupes et d'autres options de sécurité. Nous allons modifier les sections « **Blocked IPs** » et « **Authentication Options** » ; simplement suivre les étapes ci-dessous.

1. Utiliser l'option « **Text Console** » dans le logiciel Crestron Toolbox et vous brancher au MPC4-102-B via réseau ou USB.
2. Lorsque branché, utiliser l'option « **Authentication** » dans le menu « **Functions** ».
3. Sélectionner l'onglet « **Blocked IPs** ».
4. Cocher l'option « **No Limit** ».
5. Appuyer sur « **Remove Address From Blocked List** » si des adresses sont actuellement bloquées.
6. Sélectionner l'onglet « **Authentication Options** ».
7. Cocher l'option « **No Attempt Limit** ».

Si vous désirez ajouter d'autres utilisateurs, il est possible de le faire via l'onglet « **Users** ».

1. Sélectionner l'onglet « **Current User** ».
2. Appuyer sur le bouton « **Create New User** ».
3. Entrer un nom d'usager, un mot de passe et sélectionner un groupe.
4. Appuyer sur le bouton « **OK** » pour confirmer l'ajout.

## Configuration horloge du système

Suivre les étapes ci-dessous pour configurer l'heure du système.

1. Utiliser l'option « **Text Console** » dans le logiciel Crestron Toolbox et vous brancher au MPC4-102-B via réseau ou USB.
2. Lorsque branché, utiliser l'option « **System Clock** » dans le menu « **Functions** ».
3. Sélectionner le bon fuseau horaire à partir du menu déroulant « **Timezone** ».
4. Appuyer sur le bouton « **Synchronize Device Time with PC** » si vous n'utilisez pas l'option SNTP.

## Mise à jour du micrologiciel

Il est important de procéder à la mise à jour du contrôleur. Lors de l'installation, nous avons procédé à la mise à jour la plus récente du micrologiciel du MPC4-102-B disponible sur le site de Crestron.

**{{FICHIER_MICROGICIEL}}**

Pour procéder à la mise à jour du logiciel, il est possible de le faire via un fureteur web en entrant l'adresse suivante https://{{IP}} et en suivant la procédure ci-dessous :

1. Sélectionner l'option « **Update Firmware** » dans les options « **Action** » sur la page web du processeur.
2. Appuyer sur le bouton « Browse » et choisir le micrologiciel à téléverser.
3. Suivre la procédure et attendre que le processus soit terminé.

## Configuration de l'interface usager

Le MPC4-102-B comporte neuf boutons capacitifs personnalisables ainsi que les boutons dédiés de mise en marche, de volume et de sourdine avec jauge de niveau. Installer les pastilles d'icônes correspondant aux fonctions programmées, en respectant le tableau d'assignation présenté au début de ce document. La sensibilité du détecteur de proximité et la luminosité des boutons peuvent être ajustées via Crestron Toolbox ou l'interface web du processeur.

## Implantation du code

La procédure ci-dessous explique la démarche à utiliser pour implanter le code qui permettra au système d'opérer. Il est important d'implanter les fichiers de configuration avant d'implanter le code.

1. Utiliser l'option « **Text Console** » dans le logiciel Crestron Toolbox et vous brancher au MPC4-102-B via réseau ou USB.
2. Lorsque branché, utiliser l'option « **Simpl Program (Program01)** » dans le logiciel Crestron Toolbox.
3. Appuyer sur le bouton « **Browse** », choisir le fichier **{{FICHIER_PROGRAMME}}** et sélectionner « **Open** ».
4. Appuyer sur le bouton « **Send** » pour téléverser le code vers le contrôleur.
