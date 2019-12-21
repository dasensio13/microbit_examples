from microbit import *
import radio

radio.config(channel=68, power=7)
radio.on()
display.show(Image.ALL_CLOCKS, wait=False, loop=True, delay=1000)

while True:
    mensaje = radio.receive()
    if (mensaje is not None):
        display.scroll(str(mensaje))
    if (button_a.is_pressed()):
        radio.send('Hello')
        display.show(Image.YES)
    if (button_b.is_pressed()):
        radio.send('Bye bye')
        display.show(Image.NO)
    sleep(100)