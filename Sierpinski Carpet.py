# https://youtu.be/U1mxm0bLrcw

import turtle as tur
import time


def square(centre, length):
    cx, cy = centre[0], centre[1]
    length = length/3
    half_length = length/2
    if length < 2:
        return
    Ax = cx - half_length
    Ay = cy + half_length
    tur.pu()
    tur.goto(Ax, Ay)
    tur.begin_fill()
    tur.pd()
    for i in range(4):
        tur.forward(length)
        tur.right(90)
    tur.end_fill()
    square([cx-length, cy-length], length)
    square([cx, cy-length], length)
    square([cx+length, cy-length], length)
    square([cx-length, cy], length)
    square([cx+length, cy], length)
    square([cx-length, cy+length], length)
    square([cx, cy+length], length)
    square([cx+length, cy+length], length)
    square([cx, cy], length)


while True:
    tur.ht()
    tur.speed(0)
    tur.color("white")
    tur.bgcolor("black")
    square([0, 0], 648)
    time.sleep(10)
    tur.reset()
