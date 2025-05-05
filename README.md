# Binary Ninja AVR plugin
This plugin adds support for the AVR architecture to binaryninja. All instructions
should be implemented, lifting is mostly implemented.

![Disassembly](https://github.com/fluxchief/binaryninja_avr/blob/master/img/disas.png "Disassembly")
![Lifted](https://github.com/fluxchief/binaryninja_avr/blob/master/img/lifted.png "Lifted")

## Installation
Use the [plugin manager](https://docs.binary.ninja/guide/plugins.html). 

Alternatively, run this command in your BN plugins folder or download the repo into your plugin folder:
`git clone https://github.com/fluxchief/binaryninja_avr.git`

## Usage

Opening an AVR file is a bit different from other architectures in Binary Ninja due to the need to support specific chips.

You'll want to always use the "Open With Options" menu and select "AVR" from the "View Type" drop-down at the top.

Next, search for "AVR" in the settings and select the appropriate chip from the drop-down.

<!-- This URL will be broken until the PR is merged but it makes it work in the plugin manager so I think it's worth it.-->
![Open With Options](https://github.com/fluxchief/binaryninja_avr/blob/master/img/avr-open.png "Open With Options")

## How is it different than [binja_avr](https://github.com/cah011/binja-avr)?
1) This project aims for a better support of different chips. It currently has

 - ATMega16
 - ATMega168 / ATMega328
 - ATTiny48
 - ATTiny88
 - ATXMega128A4u
 - AT90CAN64

support and can be easily extended.

2) This plugin also lifts the AVR instructions. While I at first intended to add
lifting to `binja-avr`, the changes would have been to large so that I decided
to write this plugin from scratch instead.

3) Interrupt vectors are defined automatically. (currently disabled, see issue #5).

4) Xrefs on memory.

## I found a bug!
"Awesome"! Please create a ticket and don't forget to upload your sample there
as well (if possible).

## Known issues/limitations

 - RAMPX/RAMPY/RAMPZ not used - This isn't lifted as much as it could be and
   decreases the readability of the code, so I disabled the use of these
   registers.
 - Skip instruction followed by a 4 bytes instruction potentially breaks.
   This is a limitation of BN. BN only sends the raw bytes until the end of
   the basic block to the plugin, so there is no way we can figure out whether
   the length of the next instruction is 2 or 4 bytes. It seems to be 2 bytes
   most of the cases, so I hardcoded it to 2.
 - Flags aren't used properly (in lifting).

## License

[MIT](LICENSE)
