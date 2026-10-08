# Chargement d'un programme SIMPL Windows par SFTP

**Dernière révision de la section :** 2026-10-03

Procédure pour les processeurs dont le programme est livré en fichiers .lpz et .sig avec un fichier de configuration XML.

## Variables

| Variable | Description | Valeur par défaut |
|---|---|---|
| {{CONFIG_FILE}} | Fichier de configuration de salle | Room Config.xml |

## Téléversement du projet

Suivre la procédure suivante pour téléverser le nouveau projet.

- Démarrer une session ***FileZilla*** vers le processeur.
- Naviguer vers le dossier *Program01* du processeur.
- Transférer les fichiers **\*.lpz** et **\*.sig** vers le dossier *Program01*.
- Fermer la session ***FileZilla***.

<!-- IMAGE NEEDED: FileZilla, dossier Program01 (capture d'origine retirée : elle affichait le nom d'un client) -->

## Chargement du projet

Suivre la procédure suivante pour charger le nouveau projet.

- Démarrer une session ***Putty*** vers le processeur.
- Lorsque vous voyez l'invite **>**, taper la commande **progload -p:1**
- Fermer la session ***Putty*** lorsque vous voyez le message **Program(s) Started...**

## Téléversement du fichier de configuration

Suivre la procédure suivante pour téléverser le fichier de configuration.

- Démarrer une session ***FileZilla*** vers le processeur.
- Naviguer vers le dossier *NVRAM/Main* du processeur.
- Transférer le fichier **{{CONFIG_FILE}}** vers le dossier *NVRAM/Main*.
- Fermer la session ***FileZilla***.

<!-- IMAGE NEEDED: FileZilla, dossier NVRAM/Main (capture d'origine retirée : elle affichait le nom d'un client) -->

## Chargement de la configuration

Vous pouvez appuyer sur le bouton SW-R à l'avant du processeur pour redémarrer le programme, ou bien suivre la procédure suivante pour lire la nouvelle configuration sans redémarrer.

- Démarrer une session ***Putty*** vers le processeur.
- Lorsque vous voyez l'invite **>**, taper la commande **ucmd "RCF"**
- Fermer la session ***Putty*** lorsque vous voyez l'invite **>**.
