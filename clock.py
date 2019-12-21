from microbit import *
import music

clocks = [
    Image.CLOCK1,
    Image.CLOCK2,
    Image.CLOCK3,
    Image.CLOCK4,
    Image.CLOCK5,
    Image.CLOCK6,
    Image.CLOCK7,
    Image.CLOCK8,
    Image.CLOCK9,
    Image.CLOCK10,
    Image.CLOCK11,
    Image.CLOCK12
]

n = 1
clock = False
playing = False

while True:
    if (button_a.is_pressed()):
        clock = not clock
        display.show(Image.HEART)
        sleep(1000)

    if (button_b.is_pressed() and playing):
        music.stop()
        playing = False
    elif (button_b.is_pressed() and not playing):
        music.play(music.BIRTHDAY, wait=False, loop=True)
        playing = True

    if clock:
        display.show(clocks[(n % 12)], wait=False)
        n = n + 1
    elif (n > 0):
        display.scroll("Hello world!!!", wait=False, loop=True)
        n = 0
    sleep(1000)