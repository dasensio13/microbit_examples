from microbit import *
import music

do = 'C4'
re = 'D4'
mi = 'E4'
fa = 'F4'
sol = 'G4'
la = 'A4'
si = 'B4'
do2 = 'C5'
re2 = 'D5'
mi2 = 'E5'
fa2 = 'F5'
sol2 = 'G5'
la2 = 'A5'
si2 = 'B5'
silence = '0'

hand = 'left'
display.show(Image.ARROW_W)
sleep(1000)

while True:
    v1 = pin1.read_analog() > 300
    v2 = pin2.read_analog() > 300
    b1 = button_a.is_pressed()
    b2 = button_b.is_pressed()

    if (b1 and b2):
        if (hand == 'left'):
            hand = 'right'
            display.show(Image.ARROW_E)
            sleep(1000)
        else:
            hand = 'left'
            display.show(Image.ARROW_W)
            sleep(1000)

    if (b1):
        if hand == 'left':
            note = do
        else:
            note = sol
    elif (v1):
        if hand == 'left':
            note = re
        else:
            note = la
    elif (v2):
        if hand == 'left':
            note = mi
        else:
            note = si
    elif (b2):
        if hand == 'left':
            note = fa
        else:
            note = do2
    else:
        note = silence
    music.play(note, wait=False)
    display.show(note, wait=False)
    sleep(100)