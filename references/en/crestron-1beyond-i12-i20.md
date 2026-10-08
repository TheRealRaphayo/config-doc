# 1 Beyond Camera Configuration

**Reference software:** Crestron 1 Beyond Camera Manager
**Section last revised:** 2026-10-08

## Variables

| Variable | Description | Default value |
|---|---|---|
| {{AV_VLAN}} | AV network VLAN | 100 |

Default values per unit:

| Camera | IP address | Subnet mask | "Default Router" |
|---|---|---|---|
| I12 | 192.168.100.21 | 255.255.255.0 | 192.168.100.1 |
| I20 | 192.168.100.22 | 255.255.255.0 | 192.168.100.1 |
| I20 (3rd camera, additional zone) | 192.168.100.23 | 255.255.255.0 | 192.168.100.1 |

## Content

The system is equipped with Crestron 1 Beyond I12 and I20 cameras. The I12 camera is used for group framing, while the I20 camera is used for presenter framing. Configuration must be done with the Crestron 1 Beyond Camera Manager software. The following items are covered in this section:

- Network configuration.
- "Intelligent Switching" mode configuration.
- Framing zone configuration.

## Network configuration

The cameras should receive an IP address through DHCP on VLAN {{AV_VLAN}} of the network switch. To keep the rooms consistent, we will assign a static address to each camera. You can do this using the 1 Beyond Camera Manager software. The settings to configure are as follows:

{{UNIT_TABLE : Camera, IP address, Subnet mask, "Default Router"}}

<!-- IF: an I12 camera and at least one I20 camera are present -->
## "Intelligent Switching" mode configuration

To configure "Intelligent Switching" mode, connect to the I12 camera. Under "Tracking Settings", enter the IP address of the I20 camera in the "CAM 2 IP" field. Make sure to enable the "Optimize settings for multi camera" option, then confirm by clicking "Save Settings".

Make sure to enable "Tracking On" under the "POWER On State" option.

![Intelligent Switching](../../assets/images/crestron-1beyond_intelligent-switching.png)
<!-- END IF -->

## Framing zone configuration

It is important to adjust the items below:

1. Select a "Zone Profile".
2. "Set Tracking Zone".
3. "Set Tracking Shot".
   <!-- IMAGE NEEDED: Tracking Zone (original screenshot removed: view of a client's room) -->
4. Perform the "PTZ Alignment".
   <!-- IMAGE NEEDED: PTZ Alignment (original screenshot removed: view of a client's room) -->
5. Adjust the "Displays Blocking Zones B1 – B4".
6. Adjust the "Users Blocking Zones B5 – B6".
7. Adjust the "Preset Zones P1 – P4".
   <!-- IMAGE NEEDED: Preset Zones (original screenshot removed: view of a client's room) -->
8. Adjust the position of each defined "Preset Zone" by clicking the "Set Presets" button in the menu.
   <!-- IMAGE NEEDED: Set Presets (original screenshot removed: view of a client's room) -->
9. Save the adjustments with "Save Settings" before closing.
