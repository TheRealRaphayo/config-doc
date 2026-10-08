# HD-TX-4KZ-211-2G Transmitter Configuration

**Section last revised:** 2026-10-08

## Variables

| Variable | Description | Default value |
|---|---|---|
| {{LOCATION}} | Location of the wall plate | on the wall |
| {{RECEIVER}} | Device that receives the transmitter's DM Lite link | none |

## Content

The system is equipped with a Crestron HD-TX-4KZ-211-2G transmitter wall plate installed {{LOCATION}}. It provides one HDMI input and one USB-C input (DisplayPort Alt Mode) with 2x1 auto-switching, and sends the signal to the DM Lite input of the {{RECEIVER}} over a CAT5e or better cable. The transmitter does not have an IP address. The following items are covered in this section:

- Power.
- Verifying the DM Lite link.
- Auto-switching.

## Power

[TO COMPLETE: transmitter power method]

The **PWR** LED is amber during startup and green when the device is operational.

## Verifying the DM Lite link

The **LINK** LED must be green, which confirms that the DM Lite link is established with the {{RECEIVER}}. Also confirm that the LED of the input in use is green, which indicates that the source is detected and routed to the output.

## Auto-switching

The **AUTO** button on the front panel enables or disables auto-switching between the HDMI input and the USB-C input; the AUTO LED is green when the function is enabled.

## Notes

- The original document contradicts itself on two points, to be settled before fixing the text:
  - Power: it says the HD-TX-4KZ-211-2G is powered by the HD-RXC-4KZ-101, then that a 24 V power supply (sold separately) must "therefore" be connected to the transmitter's 24V 0.7A terminal. The transmitter is powered either over the link or by a local supply.
  - DM Lite link: the introduction says the signal goes to the HD-RXC-4KZ-101, while the link verification says it is established with the HD-PS402.
