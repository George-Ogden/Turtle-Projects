# https://youtu.be/rZIWzLYBPIE

import turtle as tur
import math
import time


def triangle(top, length, i=False):
    tx, ty = top[0], top[1]
    if length < 8:
        return
    tur.pu()
    if i:
        tur.goto(tx, ty)
        tur.color("white")
        tur.pd()
        tur.begin_fill()
        for i in range(3):
            tur.forward(length)
            tur.right(120)
        tur.end_fill()
    tur.goto(tx-(length/4), ty-(length*rt3/2))
    tur.color("black")
    tur.begin_fill()
    tur.goto(tx+(length/4), ty-(length*rt3/2))
    tur.goto(tx, ty-(length*rt3))
    tur.end_fill()
    triangle([tx, ty], length/2)
    triangle([tx-(length/4), ty-(length*rt3/2)], length/2)
    triangle([tx+(length/4), ty-(length*rt3/2)], length/2)


length = 380
rt3 = math.sqrt(3)/2
while True:
    tur.ht()
    tur.bgcolor("black")
    tur.seth(-60)
    tur.speed(0)
    triangle([0, length*rt3], length*2, True)
    time.sleep(10)
    tur.reset()
