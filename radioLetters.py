from microbit import *
import radio

radio.config(channel=68, power=7)
radio.on()

letters = [
    'a',
    'b',
    'c',
    'd',
    'e',
    'f',
    'g',
    'h',
    'i',
    'j',
    'k',
    'l',
    'm',
    'n',
    'o',
    'p',
    'q',
    'r',
    's',
    't',
    'u',
    'v',
    'w',
    'x',
    'y',
    'z'
    ]
index = 0
display.show(letters[index])

while True:
    mensaje = radio.receive()
    if (mensaje is not None):
        display.show(str(mensaje))
    if (button_a.is_pressed()):
        index = ((index + 1) % 26)
        display.show(letters[index])
    if (button_b.is_pressed()):
        radio.send(letters[index])
        display.show(Image.YES)
    sleep(500)