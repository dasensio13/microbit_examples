from microbit import *
import speech

text = "Hello, my name is microbit, and you can program me in python"

while True:
    sleep(1000)
    speech.say(text, speed=82, pitch=32, throat=145, mouth=145)