from microbit import *
import radio
import speech

radio.config(channel=68, power=7)
radio.on()
while True:
    sleep(100)
    mensaje = radio.receive()
    if (mensaje is not None):
        display.scroll(str(mensaje), wait=False)