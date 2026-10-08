# Loading a SIMPL Windows Program over SFTP

**Section last revised:** 2026-10-08

Procedure for processors whose program is delivered as .lpz and .sig files with an XML configuration file.

## Variables

| Variable | Description | Default value |
|---|---|---|
| {{CONFIG_FILE}} | Room configuration file | Room Config.xml |

## Uploading the project

Follow the procedure below to upload the new project.

- Start a ***FileZilla*** session to the processor.
- Browse to the *Program01* folder on the processor.
- Transfer the **\*.lpz** and **\*.sig** files to the *Program01* folder.
- Close the ***FileZilla*** session.

<!-- IMAGE NEEDED: FileZilla, Program01 folder (original screenshot removed: it showed a client's name) -->

## Loading the project

Follow the procedure below to load the new project.

- Start a ***Putty*** session to the processor.
- When you see the **>** prompt, type the command **progload -p:1**
- Close the ***Putty*** session when you see the message **Program(s) Started...**

## Uploading the configuration file

Follow the procedure below to upload the configuration file.

- Start a ***FileZilla*** session to the processor.
- Browse to the *NVRAM/Main* folder on the processor.
- Transfer the **{{CONFIG_FILE}}** file to the *NVRAM/Main* folder.
- Close the ***FileZilla*** session.

<!-- IMAGE NEEDED: FileZilla, NVRAM/Main folder (original screenshot removed: it showed a client's name) -->

## Loading the configuration

You can press the SW-R button on the front of the processor to restart the program, or follow the procedure below to read the new configuration without restarting.

- Start a ***Putty*** session to the processor.
- When you see the **>** prompt, type the command **ucmd "RCF"**
- Close the ***Putty*** session when you see the **>** prompt.
