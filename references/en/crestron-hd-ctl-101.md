# HD-CTL-101 Configuration

**Section last revised:** 2026-10-08

## Variables

| Variable | Description | Default value |
|---|---|---|
| {{CONTROLLER_IP}} | Controller IP address | the project controller's address |
| {{USERNAME}} / {{PASSWORD}} | Administrator account | none |
| {{AV_VLAN}} | AV network VLAN | 100 |

Default values per unit:

| Unit | IP-ID | IP address | Subnet mask | "Default Router" |
|---|---|---|---|---|
| Right display | 5 | 192.168.100.5 | 255.255.255.0 | 192.168.100.1 |
| Side display | 6 | 192.168.100.6 | 255.255.255.0 | 192.168.100.1 |

## Content

The system is equipped with HD-CTL-101 units for multipurpose rooms. These interfaces provide control of the displays. The following items are covered in this section:

- Network configuration and IP table

On initial startup of the interface, you are asked to enter a default password. The username and password that were configured are shown below.

**{{USERNAME}} / {{PASSWORD}}**

## Network configuration and IP table

The interfaces should receive an IP address through DHCP on VLAN {{AV_VLAN}} of the network switch. To keep the rooms consistent, we will assign a static address and an IP-ID to each interface. Make sure to use the controller IP address **{{CONTROLLER_IP}}** to allow communication. You can do this by connecting with a web browser. The settings to configure are as follows:

{{UNIT_TABLE : Interface, IP-ID, IP address, Subnet mask, "Default Router"}}
