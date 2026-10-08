# Sharp XP-V731U-W Projector Configuration

**Section last revised:** 2026-10-08

## Variables

| Variable | Description | Default value |
|---|---|---|
| {{IP}} | Static IP address | 192.168.100.21 |
| {{SUBNET_MASK}} | Subnet mask | 255.255.255.0 |
| {{GATEWAY}} | Gateway | 192.168.100.1 |
| {{HOSTNAME}} | Hostname | PROJ-01 |
| {{AV_VLAN}} | AV network VLAN | 100 |
| {{SWITCH_PORT}} | Switch port the projector is connected to | 7 |
| {{CONTROLLER}} | Control processor model | the project's controller |

## Content

The system is equipped with a Sharp XP-V731U-W projector connected over HDBaseT. The projector's network port is connected to port {{SWITCH_PORT}} of the switch, and control is done over the network from the {{CONTROLLER}} processor. The following items are covered in this section:

- Network configuration.
- Disabling the power-saving modes.
- Control configuration.

## Network configuration

The projector should receive an IP address through DHCP on VLAN {{AV_VLAN}} of the network switch. To keep the rooms consistent, we will assign the static address **{{IP}}**. Configuration is done from the projector's on-screen menu or its web interface. The settings to configure are as follows:

| Setting | Value |
|---|---|
| **IP address** | {{IP}} |
| **Subnet mask** | {{SUBNET_MASK}} |
| **Gateway** | {{GATEWAY}} |
| **Hostname** | {{HOSTNAME}} |

1. Open the projector menu and go to the network settings section ("**NETWORK SETTINGS**").
2. Disable the DHCP option and enter the settings from the table above.
3. Apply the settings and restart the projector if prompted.
4. Confirm communication with a "ping" to {{IP}} from a workstation connected to VLAN {{AV_VLAN}}.

## Disabling the power-saving modes

The power-saving functions must be disabled so that the projector stays reachable on the network and responds quickly to commands from the control system. Adjust the settings below in the projector menu:

| Setting | Value |
|---|---|
| Standby mode ("Standby Mode") | Setting that keeps the LAN port active in standby |
| Auto power off ("Auto Power Off") | Disabled |
| Off timer ("Off Timer") | Disabled |
| Light source mode ("Light Mode") | NORMAL, unless the client requires otherwise |
| Screen saver / power management | Disabled |

On the XP-V731U, the power-on command is accepted on the LAN port regardless of the standby mode setting. It is still recommended to keep the network standby mode in order to ensure a fast response and a reliable status reported to the control system.

## Control configuration

The projector is controlled over the network from the processor, at **{{IP}}**. The projector is compatible with Crestron control systems and with PJLink. If a password is configured for network access, it must be entered in the code and in the table in the appendix. Confirm that the projector selects the HDBaseT input at power-on.

## Notes

- The default address 192.168.100.21 is also the I12 camera's address in training rooms.
