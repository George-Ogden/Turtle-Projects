# https://youtu.be/RGStj_7DqqM

import turtle as tur
import time
def hex_col(color):
    return "#" + "".join([str("0"+x[x.find("x")+1:])[-2:] for x in list(map(hex,color))])
tur.bgcolor("black")
tur.speed(0)
tur.ht()
while True:
    for i in range(0,720,5):
        color = [0,0,0]
        color[(i//120+1)%3] = int((i%120)/8*17)
        color[(i//120)%3] = int(255-(i%120)/8*17)
        color = hex_col(color)
        tur.color(color)
        tur.seth(i/2)
        tur.circle(250)
    time.sleep(10)
    tur.clear()
