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

while True:
    sleep(100)
    v1 = pin1.read_analog() > 300
    v2 = pin2.read_analog() > 300
    p1 = button_a.is_pressed()
    p2 = button_b.is_pressed()
    nota = '0'
    if (p1 == False):
        if (v1 == True):
            nota = fa
        elif (v2):
            nota = sol
        elif (p2):
            nota = la
    elif (p1):
        if (v1):
            nota = do2
        elif (v2):
            nota = re2
        elif (p2):
            nota = fa2
    music.play(nota, wait=False)
    display.show(nota, wait=False)
    # music.pitch(v1)