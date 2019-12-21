from microbit import *
while True:
    v0 = pin0.read_analog()
    v1 = pin1.read_analog()
    v2 = pin2.read_analog()
    if pin0.is_touched():
        t0 = 250
    else:
        t0 = 0
    if pin1.is_touched():
        t1 = 250
    else:
        t1 = 0
    if pin2.is_touched():
        t2 = 250
    else:
        t2 = 0
    print((v0, v1, v2, t0, t1, t2))
    sleep(100)