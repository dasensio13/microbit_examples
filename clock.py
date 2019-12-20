# Escribe tu código aquí :-)
from microbit import *
import music

n = 0
clock = [
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
while True:
    sleep(100)
    v1 = pin1.read_analog()
    if pin1.is_touched():
        t1 = 200
    else:
        t1 = -200
    print((v1, t1))
    # display.scroll(str(v1))
    display.show(clock[(n % 12)], wait=False)
    if (n == 0):
        music.play(music.BLUES, wait=False, loop=True)
    n = n + 1