# LG 65PK640S0UB Display Configuration

**Section last revised:** 2026-10-08

## Variables

| Variable | Description | Default value |
|---|---|---|
| {{IP}} | Static IP address | 192.168.100.22 |
| {{SUBNET_MASK}} | Subnet mask | 255.255.255.0 |
| {{GATEWAY}} | Gateway | 192.168.100.1 |
| {{AV_VLAN}} | AV network VLAN | 100 |
| {{SWITCH_PORT}} | Switch port the display is connected to | 8 |
| {{INPUT}} | Video input in use | HDMI 1 |
| {{CONNECTION}} | Device the signal comes through (e.g. "through the Crestron HD-RXC-4KZ-101 receiver") | none |
| {{DISPLAY_ID}} | Display "Set ID" | 1 |

## Content

The system is equipped with an LG 65PK640S0UB display connected on input {{INPUT}} {{CONNECTION}}. The display's network port is connected to port {{SWITCH_PORT}} of the switch, and control is done over the network. The following items are covered in this section:

- Network configuration.
- Disabling the power-saving modes.
- Control configuration.

## Network configuration

The display should receive an IP address through DHCP on VLAN {{AV_VLAN}} of the network switch. To keep the rooms consistent, we will assign the static address **{{IP}}**. Configuration is done from the display's on-screen menu. The settings to configure are as follows:

| Setting | Value |
|---|---|
| **IP address** | {{IP}} |
| **Subnet mask** | {{SUBNET_MASK}} |
| **Gateway** | {{GATEWAY}} |

1. Open the display's settings menu and go to the network section ("**Network**" or "**Réseau**").
2. Select the wired connection (Ethernet) and choose manual address configuration.
3. Enter the settings from the table above and confirm.
4. Confirm communication with a "ping" to {{IP}} from a workstation connected to VLAN {{AV_VLAN}}.

The display also has a wireless interface; it must be disabled to avoid having two active interfaces on the same network.

## Disabling the power-saving modes

The power-saving functions must be disabled to prevent the display from turning itself off or from no longer responding to network commands. Adjust the settings below in the display menu:

| Setting | Value |
|---|---|
| Energy saving / "Energy Saving" | Disabled |
| "Smart Energy Saving" | Disabled |
| Auto power off after 4 hours | Disabled |
| Power off when no signal (15 min) | Disabled |
| Power management (DPM) | Disabled |
| Standby mode / "PM Mode" | Setting that keeps the network active in standby ("Network Ready") |
| Wake On LAN | Enabled |

The exact option names may vary depending on the webOS software version installed on the display. After configuration, confirm that the display still responds to network commands when in standby.

## Control configuration

The display is controlled over the network from the processor, at **{{IP}}**. Assign "Set ID" **{{DISPLAY_ID}}** to the display and enable network control in the menu. Disable the SIMPLINK (HDMI-CEC) function to avoid conflicts with system control. Confirm that the display returns to input {{INPUT}} after a power loss.

## Notes

- The default address 192.168.100.22 is also the I20 camera's address in training rooms.
