# Network Switch

**Reference software:** Netgear Engage
**Section last revised:** 2026-10-08

## Variables

| Variable | Description | Default value |
|---|---|---|
| {{MODEL}} | Switch model | M4250-8G2XF-PoE+ (GSM4210PX) |
| {{NETGEAR_SITE}} | Name of the Netgear Engage site template | none |
| {{SITE_PASSWORD}} | Site configuration password | none |
| {{AV_VLAN}} | AV network VLAN | 100 |

## Content

The system is equipped with a Netgear {{MODEL}} network switch. It is configured in standalone mode for AV system communication. A configuration file is available to upload to it. The following items are covered in this section:

- Netgear Engage - Importing the site.
- Netgear Engage - Assigning the switch to the site.

## Netgear Engage - Importing the site

Using the Netgear Engage software, import the {{NETGEAR_SITE}} site template. If your Netgear Engage software already has this site, you can skip this step.

1. Open Netgear Engage.
2. Go to the "Controller Management" section.
3. Select the "Import Site" option.
4. Choose the site "{{NETGEAR_SITE}}_yyyy-mm-dd_hh-mm-ss_x.zip".
5. Enter the configuration password "{{SITE_PASSWORD}}".
6. Click "Upload".

<!-- IF: the switch must be assigned to the site in Netgear Engage -->
## Netgear Engage - Assigning the switch to the site

Once the site has been added to your Netgear Engage software, you can use it on the switch. Make sure to select the correct network interface. Follow the steps below:

1. In the "Devices" menu, select the site from the drop-down menu.
2. In the "Discovered Devices" menu, click "Onboard" to add the switch.

Once the switch has been assigned, it should be configured according to the configuration template for this room type. Ports 1 to 3 and 5 to 8 are assigned to AV VLAN {{AV_VLAN}}. Ports 4, 9 and 10 remain on "Management" VLAN 1.

<!-- IMAGE NEEDED: switch port view in Netgear Engage (original screenshot removed: it showed the client's site name) -->
<!-- END IF -->
