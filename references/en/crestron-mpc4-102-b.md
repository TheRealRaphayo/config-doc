# Crestron MPC4-102-B Controller Configuration

**Reference firmware version:** mpc4-mpb4_2.8006.00322.01.puf
**Section last revised:** 2026-10-08

## Variables

| Variable | Description | Default value |
|---|---|---|
| {{IP}} | Static IP address of the controller | 192.168.100.2 |
| {{SUBNET_MASK}} | Subnet mask | 255.255.255.0 |
| {{GATEWAY}} | "Default Router" | 192.168.100.1 |
| {{HOSTNAME}} | Hostname | MPC-01 |
| {{USERNAME}} / {{PASSWORD}} | Administrator account | none |
| {{AV_VLAN}} | AV network VLAN | 100 |
| {{FIRMWARE_FILE}} | Installed firmware file | none |
| {{PROGRAM_FILE}} | Program file (.lpz) | none |

## Content

The following items are covered in this section.

- Network configuration.
- Authentication configuration.
- System clock configuration.
- Firmware update.
- User interface configuration.
- Loading the code.

On initial startup of the processor, you are asked to enter a default password. The username and password that were configured are shown below.

**{{USERNAME}} / {{PASSWORD}}**

## Network configuration

The processor should receive an IP address through DHCP on VLAN {{AV_VLAN}} of the network switch. To keep the rooms consistent, we will assign the static address **{{IP}}**. You can do this using Crestron Toolbox.

1. Use the "**Text Console**" option in the Crestron Toolbox software and connect to the MPC4-102-B over the network or USB.
2. Once connected, use the "**Ethernet Addressing**" option in the "**Functions**" menu.
3. Check the "**IP Static**" option and enter the settings below:

| Setting | Value |
|---|---|
| **IP address** | {{IP}} |
| **Subnet mask** | {{SUBNET_MASK}} |
| **"Default Router"** | {{GATEWAY}} |
| **Hostname** | {{HOSTNAME}} |

4. When done, click "**Apply**" and the processor will reboot.

## Authentication configuration

It is recommended to configure the authentication options. You can add users, groups and other security options. We will modify the "**Blocked IPs**" and "**Authentication Options**" sections; simply follow the steps below.

1. Use the "**Text Console**" option in the Crestron Toolbox software and connect to the MPC4-102-B over the network or USB.
2. Once connected, use the "**Authentication**" option in the "**Functions**" menu.
3. Select the "**Blocked IPs**" tab.
4. Check the "**No Limit**" option.
5. Click "**Remove Address From Blocked List**" if any addresses are currently blocked.
6. Select the "**Authentication Options**" tab.
7. Check the "**No Attempt Limit**" option.

If you want to add other users, you can do so from the "**Users**" tab.

1. Select the "**Current User**" tab.
2. Click the "**Create New User**" button.
3. Enter a username, a password and select a group.
4. Click the "**OK**" button to confirm.

## System clock configuration

Follow the steps below to set the system time.

1. Use the "**Text Console**" option in the Crestron Toolbox software and connect to the MPC4-102-B over the network or USB.
2. Once connected, use the "**System Clock**" option in the "**Functions**" menu.
3. Select the correct time zone from the "**Timezone**" drop-down menu.
4. Click the "**Synchronize Device Time with PC**" button if you are not using the SNTP option.

## Firmware update

It is important to update the controller. During installation, we applied the most recent firmware update for the MPC4-102-B available on the Crestron website.

**{{FIRMWARE_FILE}}**

The update can be done from a web browser by entering the address https://{{IP}} and following the procedure below:

1. Select the "**Update Firmware**" option under "**Action**" on the processor web page.
2. Click the "**Browse**" button and choose the firmware to upload.
3. Follow the procedure and wait for the process to finish.

## User interface configuration

The MPC4-102-B has nine customizable capacitive buttons as well as dedicated power, volume and mute buttons with a level gauge. Install the icon caps matching the programmed functions, following the assignment table shown at the beginning of this document. The proximity sensor sensitivity and the button brightness can be adjusted using Crestron Toolbox or the processor web interface.

## Loading the code

The procedure below explains how to load the code that allows the system to operate. It is important to load the configuration files before loading the code.

1. Use the "**Text Console**" option in the Crestron Toolbox software and connect to the MPC4-102-B over the network or USB.
2. Once connected, use the "**Simpl Program (Program01)**" option in the Crestron Toolbox software.
3. Click the "**Browse**" button, choose the file **{{PROGRAM_FILE}}** and select "**Open**".
4. Click the "**Send**" button to upload the code to the controller.
