# QSC Audio Processor Configuration

**Reference software version:** Q-SYS Designer 10.4.0
**Section last revised:** 2026-10-08

## Variables

| Variable | Description | Default value |
|---|---|---|
| {{IP}} | Static IP address of the processor | 192.168.100.10 |
| {{SUBNET_MASK}} | Subnet mask | 255.255.255.0 |
| {{GATEWAY}} | "Default Router" | 192.168.100.1 |
| {{AV_VLAN}} | AV network VLAN | 100 |
| {{QSYS_VERSION}} | Software version used at deployment | 10.4.0 |

## Content

The system is equipped with a QSC audio processor that handles audio integration of the various sources and destinations. You will need the Q-SYS Designer software for the following steps. The following items are covered in this section:

- Network configuration.
- Assigning the system name.
- Loading the audio design file.
- Configuration of the audio channels and controls.

## Network configuration

The processor should receive an IP address through DHCP on VLAN {{AV_VLAN}} of the network switch. To keep the rooms consistent, we will assign the static address **{{IP}}**. You can do this using the Q-SYS Designer software or a web browser. The settings to configure are as follows:

| Setting | Value |
|---|---|
| **IP address** | {{IP}} |
| **Subnet mask** | {{SUBNET_MASK}} |
| **"Default Router"** | {{GATEWAY}} |

## Assigning the system name

There are several systems and each of them should have a different configuration. It is important that each room has its own DSP design file. A template design file is used as a reference: rename the Q-SYS processor and save the template design file under another name that includes the room information (floor, room number, room name, etc.).

## Loading the audio design file

Follow the usual procedure to load the audio design file into the DSP. At initial deployment, the software version used is {{QSYS_VERSION}}.

## Configuration of the audio channels and controls

It is important to configure the audio channel used for the microphones; see the image below.

![Microphone audio channel](../../assets/images/qsc-core_canal-microphones.png)

<!-- IF: Sennheiser TCCM ceiling microphones are present -->
It is also important to enter the API control information of the Sennheiser ceiling microphones in the control blocks. See the image below.

![TCCM control blocks](../../assets/images/qsc-core_blocs-tccm.png)

<!-- IMAGE NEEDED: IP Address / Username / Password fields of the control block (original screenshot removed: it showed a password) -->
<!-- END IF -->
