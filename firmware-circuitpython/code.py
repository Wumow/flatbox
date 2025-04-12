import digitalio
import board
import struct
import usb_hid


def prepare_pin(p):
    pin = digitalio.DigitalInOut(p)
    pin.direction = digitalio.Direction.INPUT
    pin.pull = digitalio.Pull.UP
    return pin


dpad_pins = [prepare_pin(p) for p in [board.LEFT, board.RIGHT, board.UP, board.DOWN]]
button_pins = [
    prepare_pin(p)
    for p in [
        board.SQUARE,
        board.CROSS,
        board.CIRCLE,
        board.TRIANGLE,
        board.L1,
        board.R1,
        board.L2,
        board.R2,
        board.OPT2,
        board.OPT1,
        board.OPT5,
        board.OPT6,
        board.OPT3,
        board.OPT4,
    ]
]

dpad_lut = [
    0x0F,
    0x06,
    0x02,
    0x0F,
    0x00,
    0x07,
    0x01,
    0x00,
    0x04,
    0x05,
    0x03,
    0x04,
    0x0F,
    0x06,
    0x02,
    0x0F,
]

prev_report = None

while True:
    buttons = sum([((0 if pin.value else 1) << i) for i, pin in enumerate(button_pins)])
    dpad = dpad_lut[
        sum([((0 if pin.value else 1) << i) for i, pin in enumerate(dpad_pins)])
    ]
    report = struct.pack("<HBBBBBB", buttons, dpad, 0x80, 0x80, 0x80, 0x80, 0)
    if report != prev_report:
        usb_hid.devices[0].send_report(report)
    prev_report = report
