from microbit import *

def imageFromVolt(volt):
    volt = volt * 5 / 1023
    if volt < 1:
        num = int(volt*10)
        imagePin = "0000" + str(num)
    elif volt < 2:
        num = int((volt-1)*10)
        imagePin = "000" + str(num) + "9"
    elif volt < 3:
        num = int((volt-2)*10)
        imagePin = "00" + str(num) + "99"
    elif volt < 4:
        num = int((volt-3)*10)
        imagePin = "0" + str(num) + "999"
    else:
        num = int((volt-4)*10)
        imagePin = str(num) + "9999"
    return imagePin

while True:
    imagePin0 = imageFromVolt(pin0.read_analog())
    imagePin1 = imageFromVolt(pin1.read_analog())
    imagePin2 = imageFromVolt(pin2.read_analog())
    imageHist = "00000:" + imagePin0 + ":" + imagePin1 + ":" + imagePin2 + ":00000"
    display.show(Image(imageHist))
    sleep(100)


