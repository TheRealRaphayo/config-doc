# Sennheiser TCCM Ceiling Microphone Configuration

**Reference software:** Sennheiser Control Cockpit, Dante Controller
**Section last revised:** 2026-10-08

## Variables

| Variable | Description | Default value |
|---|---|---|
| {{AV_VLAN}} | AV network VLAN | 100 |
| {{API_USERNAME}} | Control API username | api |
| {{API_PASSWORD}} | Control API password | none |

No default address per unit: the original documents contradict each other (see "Notes"). The addresses come from the equipment list.

## Content

The system is equipped with Sennheiser TCCM ceiling microphone(s) for audio pickup. You will need the Sennheiser Control Cockpit software as well as the Dante Controller software for configuration. The following items are covered in this section:

- Control and audio network configuration.
- Software update.
- Enabling the control API.
- Assigning the audio references.

## Control and audio network configuration

The ceiling microphone(s) should receive an IP address through DHCP on VLAN {{AV_VLAN}} of the network switch. To keep the rooms consistent, we will assign a static address to each ceiling microphone. You can do this using the Sennheiser Control Cockpit software. The settings to configure are as follows:

{{UNIT_TABLE : Microphone, Control IP address, Subnet mask, "Default Router"}}

It is not necessary to configure the IP address for audio, because VLAN {{AV_VLAN}} provides DHCP.

![Network settings](../../assets/images/sennheiser-tccm_reseau.png)

## Software update

Make sure to update the ceiling microphone software using Sennheiser Control Cockpit.

## Enabling the control API

Make sure to enable the control API in the ceiling microphones and to use the password "{{API_PASSWORD}}". The username should be "{{API_USERNAME}}".

<!-- IMAGE NEEDED: Access / Secure API tab (original screenshot removed: it showed a password) -->

## Assigning the audio references

Section to be completed.

## Notes

- In the original documents, this section gave the control addresses 192.168.100.5 and .6 with gateway 192.168.100.254, while the appendix gave 192.168.100.31 and .32 with gateway 192.168.100.1 (and .5/.6 are also used by the HD-CTL-101 units). To be settled before adding default values.
