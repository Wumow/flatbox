# Flatbox rev4.1 WASD

This is rev4.1 of the Flatbox, WASD edition. In this version the PCB includes the microcontroller (RP2040) - everything is built in, you only have to add the switches (and flash the firmware). It has a USB Type A host port that you can use to plug in authentication dongles or other devices if the firmware you use supports that.

There are two variants of the case, version A uses flaps for the option buttons, version B has holes so that you can use buttoncaps on the tact switches:

![Flatbox rev4.1 case variants](images/Flatbox-rev4.1wasd-variants.png)

To make one you will need:

* [3D printed](3d-printed-case) case parts - top and bottom
* [the PCB](pcb)
* 13x Kailh low profile (choc v1) switches of your choice
* (optionally) 13x Kailh low profile hotswap sockets
* buttoncaps for the action buttons, either [3D printed](../3d-printed-buttoncaps) or (preferably) injection molded (make sure they're the correct size: 22.5mm and 28.5mm)
* keycaps for the WASD section (we don't have a 3D printed version, they're widely available on AliExpress etc.)
* for case variant A:
  * 6x 6x6x5mm tact switches
* for case variant B:
  * 6x 6x6x7mm tact switches
  * 6x silicone buttoncaps (like [these](https://www.aliexpress.com/item/32846395636.html) or search for "silicone button caps" on AliExpress; or you can use other caps as long as they fit, the hole diameter is 7.5mm)
* 7x M3x6 flat head (countersunk) screws
* 5x M2x4 screws to secure the PCB to the case
* some kind of rubber feet or non-slip padding for the bottom
* a soldering iron

I printed the case at 0.20mm layer height. The top part should be printed upside-down, the bottom part should be printed as-is. They don't require supports.

I used [JLCPCB](https://jlcpcb.com/) to make the PCB and assemble the SMD parts. The [included files](pcb) can be used with JLCPCB directly. If you want to use some other service, check the file formats that they expect. When ordering from JLCPCB, upload the Gerber zip, leave all the settings at default (you can choose the PCB color), then enable "PCB Assembly" and upload the BOM and CPL files in the next step. PCB thickness should be 1.6mm.

The PCB you get from JLCPCB will look something like this:

![Flatbox rev4.1 WASD PCB with SMD parts assembled](images/Flatbox-rev4.1wasd-pcb-with-smd-parts.jpg)

The switches can be soldered in directly to the PCB or you can use hotswap sockets.

For the firmware you probably want to use [GP2040-CE](https://gp2040-ce.info/). Go to the [GP2040-CE downloads page](https://gp2040-ce.info/downloads/) and get the UF2 file for Flatbox rev4.

To flash the firmware, connect the PCB to a computer with a USB cable, then press the RESET button while holding the BOOT button on the PCB. A drive named "RPI-RP2" should appear. Copy the UF2 file you downloaded to that drive. That's it.

You will have to configure the thumb button yourself as it has no preset function. It can be mapped separately from the WASD "up" button (it's wired to GPIO17).

(Of course you can also use any other RP2040-compatible firmware if you want.)

If you want to use the USB host port and you need to configure it in your firmware, D+ is connected to GPIO20 and D- to GPIO21.

If you want to modify the case or the PCB, check out the files in the [extras](extras) folder.

![Flatbox rev4.1 WASD exploded view of the 3D printed case](images/Flatbox-rev4.1wasd-exploded.png)

PCB design licensed under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).

PCB design uses the following libraries:

* [keyswitches.pretty](https://github.com/daprice/keyswitches.pretty) by [daprice](https://github.com/daprice) ([CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/))
* [Type-C.pretty](https://github.com/ai03-2725/Type-C.pretty) by [ai03-2725](https://github.com/ai03-2725)
* RP2040 library from the [minimal design example](https://datasheets.raspberrypi.org/rp2040/Minimal-KiCAD.zip) from the [Hardware design with RP2040](https://datasheets.raspberrypi.org/rp2040/hardware-design-with-rp2040.pdf) document
