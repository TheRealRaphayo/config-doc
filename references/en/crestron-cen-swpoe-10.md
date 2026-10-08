# Network Switch

**Section last revised:** 2026-10-08

## Variables

| Variable | Description | Default value |
|---|---|---|
| {{IP}} | Static IP address of the switch (AV VLAN gateway) | 192.168.100.1 |
| {{SUBNET_MASK}} | Subnet mask | 255.255.255.0 |
| {{HOSTNAME}} | Hostname | SW-01 |
| {{AV_VLAN}} | AV network VLAN | 100 |
| {{CONTROLLER}} | Model of the PoE-powered controller | the project's controller |

## Content

The system is equipped with a Crestron CEN-SWPOE-10 network switch. It is a ten-port managed switch, eight ports of which provide PoE+ (802.3at, up to 30 W per port), plus two SFP+ ports. It is configured in standalone mode for AV system communication and powers the {{CONTROLLER}} keypad. The following items are covered in this section:

- Switch network configuration.
- Port and PoE configuration.
- Configuration backup.

## Switch network configuration

The switch acts as the gateway for AV VLAN {{AV_VLAN}}. To keep the rooms consistent, we will assign it the static address **{{IP}}**. By default, the switch obtains its address through DHCP, or uses the address 169.254.100.100 if there is no DHCP; configuration is then done through its web interface.

1. Connect a workstation to a port on the switch and find the address obtained through DHCP.
2. Open a web browser and enter the switch address.
3. Log in with the configured username and password (see the table in the appendix).
4. In the network configuration section, select static addressing and enter the settings below:

| Setting | Value |
|---|---|
| **IP address** | {{IP}} |
| **Subnet mask** | {{SUBNET_MASK}} |
| **Hostname** | {{HOSTNAME}} |

5. Apply and save the configuration; the switch will then be reachable at {{IP}}.

## Port and PoE configuration

All AV devices in the room are connected to VLAN {{AV_VLAN}}. Make sure PoE is enabled on the port of the {{CONTROLLER}} keypad, since it has no other power source. The port assignment is as follows:

<!-- INSTRUCTION: the table below is the port assignment of the standard presentation room. Remove the rows for equipment that is not in the list. If the user provides a different assignment, use it. If the list contains network devices that are not in this table, ask the user for their port. -->

| Port | Device |
|---|---|
| 1 | Crestron HD-PS402 |
| 2 | Crestron MPC4-102-B (PoE+ required) |
| 3 to 6 | Spare – additional AV devices |
| 7 | Sharp XP-V731U-W |
| 8 | LG 65PK640S0UB |
| 9 and 10 (SFP+) | Uplink to the corporate network, if required |

## Configuration backup

Once the configuration is complete, export the switch configuration file and keep it with the room documentation. This file can be re-imported when the equipment is replaced.
