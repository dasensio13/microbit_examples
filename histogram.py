# Add your Python code here. E.g.
from microbit import *
import music

def cadenaImagen(voltios):
    voltios = voltios * 5 / 1023
    if voltios < 1:
        numero = int(voltios*10)
        cadenaPin = "0000" + str(numero)
    elif voltios < 2:
        numero = int((voltios-1)*10)
        cadenaPin = "000" + str(numero) + "9"
    elif voltios < 3:
        numero = int((voltios-2)*10)
        cadenaPin = "00" + str(numero) + "99"
    elif voltios < 4:
        numero = int((voltios-3)*10)
        cadenaPin = "0" + str(numero) + "999"
    else:
        numero = int((voltios-4)*10)
        cadenaPin = str(numero) + "9999"
    return cadenaPin

def cadenaImagenFacil(voltios):
    voltios = voltios * 5 / 1023
    if voltios < 1:
        cadenaPin = "00009"
    elif voltios < 2:
        cadenaPin = "00099"
    elif voltios < 3:
        cadenaPin = "00999"
    elif voltios < 4:
        cadenaPin = "09999"
    else:
        cadenaPin = "99999"
    return cadenaPin

notas = {"000": "0", "001": "A", "010": "B", "100": "C", "011": "D"}
notas["110"] = "E"
notas["101"] = "F"
notas["111"] = "G"

while True:
    v1 = pin1.read_analog()
    v2 = pin2.read_analog()
    if button_a.is_pressed():
        numero1 = "1"
    else:
        numero1 = "0"
    if button_b.is_pressed():
        numero2 = "1"
    else:
        numero2 = "0"
    if v1 > 300:
        numero3 = "1"
    else:
        numero3 = "0"
    numero = numero1 + numero2 + numero3
    music.play(notas[numero])
    # isplay.show(notas[numero])
    cadenaPin1 = cadenaImagen(v1)
    cadenaPin2 = cadenaImagen(v2)
    cadena = "00000:00000:" + cadenaPin1 + ":" + cadenaPin2 + ":00000"
    histograma = Image(cadena)
    display.show(histograma)
    sleep(10)



