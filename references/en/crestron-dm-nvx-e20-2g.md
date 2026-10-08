# DM-NVX-E20-2G Encoder

**Section last revised:** 2026-10-08

## Variables

| Variable | Description | Default value |
|---|---|---|
| {{USERNAME}} / {{PASSWORD}} | Login account | none |
| {{LOCATION}} | Location and role of the units in the room (e.g. "in the AV cabinet for content sharing") | none |
| {{AV_VLAN}} | AV network VLAN | 100 |
| {{SUBNET}} | First three octets of the AV network | 192.168.100 |

The IP addresses and IP-IDs of each unit are listed in the table in the appendix.

## Content

The encoder wall plates are located {{LOCATION}}. The plates are powered by PoE through the network port they are connected to. This section covers the items below:

- IP address range
- Login account
- IP table configuration
- Settings configuration

## IP address range

The E20-2G encoders should receive an IP address through DHCP on VLAN {{AV_VLAN}} of the network switch. See the table in the appendix for more information.

## Login account

The default account has been replaced with the information below:

**{{USERNAME}} / {{PASSWORD}}**

To access the configuration options of each unit, you can use the DM NVX Tool application or a web browser by entering the following address: https://{{SUBNET}}.x.

![Login page](../../assets/images/crestron-dm-nvx_connexion.png)

## IP table configuration

Each unit needs a unique ID to communicate with the processor. See the table in the appendix for more information. You can assign the ID using Crestron Toolbox, DM NVX Tool, or the unit's web interface by selecting "Settings" and choosing the "Control System" section.

![IP table](../../assets/images/crestron-dm-nvx_table-ip.png)

## Settings configuration

The configuration of the various settings is shown below:

| Setting | Value |
|---|---|
| Stream Status | D10/D20 |
| Input1 EDID | DM Default |
| Input1 HDCP | Disabled |
