# HD-PS402 Presentation System Configuration

**Reference firmware version:** hd-ps401_hd-ps402_hd-ps621_hd-ps622_1.4.4790.00075.puf
**Section last revised:** 2026-10-08

## Variables

| Variable | Description | Default value |
|---|---|---|
| {{IP}} | Static IP address | 192.168.100.10 |
| {{SUBNET_MASK}} | Subnet mask | 255.255.255.0 |
| {{GATEWAY}} | "Default Router" | 192.168.100.1 |
| {{USERNAME}} / {{PASSWORD}} | Administrator account | none |
| {{AV_VLAN}} | AV network VLAN | 100 |
| {{FIRMWARE_FILE}} | Installed firmware file | none |
| {{CONTROLLER}} | Control processor model | the project's controller |
| {{CONTROLLER_IP}} | Control processor IP address | the project controller's address |
| {{AMPLIFIER}} | Model of the amplifier fed by the AUX output | the project's amplifier |

## Content

The system is equipped with a Crestron HD-PS402 presentation system providing four HDMI inputs and two HDMI outputs with mirrored DM Lite outputs. It handles automatic source switching, scaling to the display, EDID management, and audio mixing and de-embedding. The following items are covered in this section:

- Network configuration.
- Firmware update.
- Auto-switching and EDID configuration.
- Audio configuration.
- IP table configuration.

On initial startup of the device, you are asked to enter a default password. The username and password that were configured are shown below.

**{{USERNAME}} / {{PASSWORD}}**

## Network configuration

The device should receive an IP address through DHCP on VLAN {{AV_VLAN}} of the network switch. To keep the rooms consistent, we will assign the static address **{{IP}}**. You can do this through the device's web interface or with Crestron Toolbox. The settings to configure are as follows:

| Setting | Value |
|---|---|
| **IP address** | {{IP}} |
| **Subnet mask** | {{SUBNET_MASK}} |
| **"Default Router"** | {{GATEWAY}} |

## Firmware update

Update the HD-PS402 with the most recent version available on the Crestron website, using the "**Update Firmware**" option in the device's web interface.

**{{FIRMWARE_FILE}}**

## Auto-switching and EDID configuration

Auto-switching and EDID management are configured from the HD-PS402 web interface. Follow the steps below:

1. In the inputs section, enable auto-switching and choose the desired mode: either the last connected input or the priority assigned to each input.
2. Assign the priority of each input according to how the room is used.
3. Confirm that the input connected to the wall plate is included in auto-switching.
4. In the EDID section, assign an EDID that matches the capability of the installed display.
5. Save the configuration.

## Audio configuration

<!-- IF: an amplifier is connected to the AUX output -->
The HD-PS402 de-embeds the audio of the selected source and routes it to the AUX output, which feeds the {{AMPLIFIER}} amplifier. Adjust the mixer of the output in use, set the output level, and confirm that the connection mode, balanced or unbalanced, matches the wiring to the amplifier. The volume adjustment range used by the code must also be validated to avoid clipping.
<!-- END IF -->

## IP table configuration

Configure the HD-PS402 IP table to communicate with the {{CONTROLLER}} processor at **{{CONTROLLER_IP}}**. See the table in the appendix for the IP-ID to use. You can assign the ID using Crestron Toolbox or the device's web interface.

## Notes

- The original document used IP-ID 05 and added that the HD-PS402 "hosts the configuration of the HD-TX-4KZ-211-2G transmitter"; that sentence was removed from the generic text, to be restored if it applies to every room.
- The default address 192.168.100.10 is also the QSC Core's address in training rooms.
