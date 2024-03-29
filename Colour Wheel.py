# https://youtu.be/7_EMslgw3cE

import turtle as tur
import math
import time


def hex_col(color):
    return "#" + "".join([str("0"+x[x.find("x")+1:])[-2:] for x in list(map(hex, color))])


def get_col_ang(x, y):
    return math.atan(x/y) * 360 / math.pi


def get_col(theta):
    color = [0, 0, 0]
    color[int(theta//120)] = int((theta % 120)/8*17)
    color[int(theta//120-1)] = int(255-(theta % 120)/8*17)
    return hex_col(color)


def circle(angle, radius, pos=(0, 0)):
    tur.pu()
    tur.goto(*pos)
    tur.pd()
    tur.seth(angle)
    for i in range(0, 360, 1):
        if i == 0:
            tur.color(get_col(angle))
        else:
            tur.color(get_col(get_col_ang(*tur.pos())))
        tur.circle(radius, 1)


while True:
    tur.bgcolor("black")
    tur.speed(0)
    tur.ht()
    for i in range(0, 720, 5):
        circle(i/2, 240)
    time.sleep(10)
    tur.reset()
