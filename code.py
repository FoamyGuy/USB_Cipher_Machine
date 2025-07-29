import time

import board
import keypad
import supervisor
import sys
import usb_hid

from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
import adafruit_ht16k33.segments
from fizzbuzz_cipher import FizzBuzzCipher


starttime = time.monotonic()
use_usb_hid = False

# wait a bit for USB to be connected
while time.monotonic() < starttime + 5:
    if supervisor.runtime.usb_connected:
        use_usb_hid = True
        break

# initialize the cipher object
cipher = FizzBuzzCipher("fizzbuzz.keys")
# initialize the display
i2c = board.I2C()
display = adafruit_ht16k33.segments.Seg14x4(i2c)
display.brightness = 0.3
# setup input for mode button
mode_btn = keypad.Keys((board.BUTTON,), value_when_pressed=False, pull=True)

# if USB was connected initialize the HID output stuff
if use_usb_hid:
    keyboard = Keyboard(usb_hid.devices)
    layout = KeyboardLayoutUS(keyboard)

# state machine variables
MODE_ENCRYPT = 0
MODE_DECRYPT = 1
mode = MODE_ENCRYPT

# buffer for currently shown on the display
displaybuffer = ""

def show_text(segment_display, text):
    """
    Show some text on the display
    """
    try:
        for i in range(4):
            segment_display[i] = text[i]
    except IndexError:
        pass

while True:
    # check for incoming data from USB Host keyboard
    available = supervisor.runtime.serial_bytes_available
    if available:  # if a key was pressed
        # read which key it was
        c = sys.stdin.read(available)

        if mode == MODE_ENCRYPT:
            # encrypt it
            cipherchr = cipher.encrypt(c)

            if use_usb_hid:
                # output ciphertext out from HID to the computer
                layout.write(cipherchr)
            else:
                # No HID connection, so output ciphertext to the display instead
                displaybuffer += cipherchr
                displaybuffer = displaybuffer[-4:]
                show_text(display, displaybuffer)

        elif mode == MODE_DECRYPT:
            # decrypt it
            clearchr = cipher.decrypt(c)

            # show the cleartext on the display
            displaybuffer += clearchr
            displaybuffer = displaybuffer[-4:]
            show_text(display, displaybuffer)

    # check for mode button press
    event = mode_btn.events.get()
    # event will be None if nothing has happened.
    if event and event.released:
        if mode == MODE_ENCRYPT:
            show_text(display, "Dec ")
            mode = MODE_DECRYPT
            displaybuffer = ""
            cipher.reset_keys()
            time.sleep(1)
            display.fill(0)
        elif mode == MODE_DECRYPT:
            show_text(display, "Enc ")
            mode = MODE_ENCRYPT
            cipher.reset_keys()
            time.sleep(1)
            display.fill(0)

