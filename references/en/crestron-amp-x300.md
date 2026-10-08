# AMP-X300 Amplifier Configuration

**Section last revised:** 2026-10-08

## Variables

| Variable | Description | Default value |
|---|---|---|
| {{AUDIO_SOURCE}} | Device that feeds the amplifier | the project's (e.g. HD-PS402) |

## Content

The system is equipped with a Crestron AMP-X300, a four-channel amplifier with 300 W of total power. It has no network interface; all configuration is done from the front-panel controls and the wiring. The following items are covered in this section:

- Output mode selection.
- Gain adjustment.
- Standby mode.

## Output mode selection

The front-panel switches configure the channel pairs for low impedance (4 or 8 ohms), bridged mode, or high impedance (70 V / 100 V). Select the mode that matches the installed loudspeakers **before** powering on the amplifier, then confirm the output wiring.

## Gain adjustment

Each channel has an independent gain adjustment. First set the output level of the {{AUDIO_SOURCE}}, then adjust the amplifier gains to obtain the desired level in the room without clipping. Record the final positions in the room documentation.

## Standby mode

The **REMOTE** input accepts a dry contact closure that places the outputs in standby. If this function is used, connect it to a relay on the control system. Otherwise, the amplifier goes into standby automatically after a period without signal and wakes up as soon as a signal is detected.
