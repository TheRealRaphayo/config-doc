# Program: training and multipurpose room

**Section last revised:** 2026-10-08

This section describes the control program, not a piece of equipment. It provides two parts of the document: "System Information" (at the beginning) and "Software Configuration" (after the equipment).

## System Information

This is the functionality of the training and multipurpose room model. The system runs in automatic mode and the displays turn on according to the state of the Crestron UC-CX100-T. An advanced control page is available to adjust the microphone(s). When the system returns to standby, custom microphone level adjustments are reset to their default value.

### Room control page

The system has a control page for the wireless microphone and the camera system. The camera system should always be in automatic switching mode. Manual control lets the user take over. The system returns to automatic mode when a call is started. This page automatically returns to the meeting controls after a 60-second delay or when the user presses the Home button.

![Room control page](../../assets/images/programme-salle-formation_page-controle.png)

## Software Configuration

### Configuration file

On the initial upload of the system, the configuration file is automatically created in the processor's User folder.

### User console commands

When you are on the processor console, typing "Help user" shows a list of commands created for debugging.

| Command | Description |
|---|---|
| Basecfg -show | Shows the configuration file. |
| Dsp -report | Shows the DSP information. |
| Maincam -report | Shows the I12 camera information. |
| Room -cfg | Shows the room configuration. |
| Trackcam -report | Shows the I20 camera information. |
| Uce -report | Shows the UC-Engine information. |
| Videodisplay -on | Turns the display on. |
| Videodisplay -off | Turns the display off. |
