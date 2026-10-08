# Program: presentation room

**Section last revised:** 2026-10-08

This section describes the control program, not a piece of equipment. It provides two parts of the document: "System Information" (at the beginning) and "Software Configuration" (after the equipment).

## System Information

This is the functionality of the presentation room model. The system is standalone and has no integrated conferencing system. The local sources and the table wall plate are routed to the Crestron HD-PS402 presentation system, which auto-switches to the projector and the display. Program audio is de-embedded by the HD-PS402 and routed to the Crestron AMP-X300 amplifier. Room control is provided by the Crestron MPC4-102-B processor keypad. When the system returns to standby, volume adjustments are reset to their default value. The system turns on automatically when it detects a source. The system turns off automatically after 60 seconds when no source is detected.

The equipment covered by this document is listed below:

<!-- INSTRUCTION: keep only the rows for equipment present in the list. For a piece of equipment in the list that is not in this table, add a row with the description given in the list. -->

| Equipment | Description |
|---|---|
| Crestron CEN-SWPOE-10 | 10-port managed network switch, PoE+ on 8 ports |
| Crestron MPC4-102-B | 4-Series processor and wall-mount control keypad |
| Crestron HD-PS402 | 4x2 4K60 4:4:4 presentation system |
| Crestron HD-TX-4KZ-211-2G | DM Lite transmitter wall plate, HDMI and USB-C |
| Crestron AMP-X300 | Four-channel amplifier, 300 W |
| Crestron HD-RXC-4KZ-101 | DM Lite receiver with CEC, IR and RS-232 control |
| Sharp XP-V731U-W | WUXGA laser projector, connected over HDBaseT |
| LG 65PK640S0UB | 65-inch UHD display |

### Room control interface

The system is equipped with a Crestron MPC4-102-B keypad that combines the 4-Series control processor and the user interface in a single device. The capacitive buttons provide source selection, system power on and off, and volume adjustment. The proximity sensor wakes the interface when a user approaches, and the button brightness adjusts automatically to the room lighting.

The keypad button assignment is as follows:

<!-- INSTRUCTION: default assignment of the program. If the user provides a different assignment, use it. -->

| Button | Function |
|---|---|
| 1 | Wall plate HDMI & USB-C |
| 2 | Wall plate HDMI |
| 3 | HDMI 3 (Not used). |
| 4 | HDMI 4 (Not used). |
| Power | System power on and off |
| Volume and mute | Program level adjustment and mute |

## Software Configuration

### Configuration file

On the initial upload of the system, the configuration file is automatically created in the processor's User folder.

### User console commands

No user commands are available in this system.
