from microbit import *

while True:
    if button_a.is_pressed():
        display.scroll(temperature())
    if button_b.is_pressed():
        display.scroll(display.read_light_level())