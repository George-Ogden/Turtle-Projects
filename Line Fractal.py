# https://youtu.be/Rg-IVdXFi0M

import time
import math
import turtle


def line(startx, starty, endx, endy):
    fullx = endx-startx
    fully = endy-starty
    distance = math.sqrt(fully**2+fullx**2)
    if distance < 6:
        turtle.penup()
        turtle.goto(startx, starty)
        turtle.pendown()
        turtle.goto(endx, endy)
        return
    thirdx = fullx/3
    thirdy = fully/3
    Ax = startx+thirdx
    Ay = starty+thirdy
    Cx = endx-thirdx
    Cy = endy-thirdy
    Bx = Ax-thirdy
    By = Ay+thirdx
    Dx = Cx+thirdy
    Dy = Cy-thirdx
    line(startx, starty, Ax, Ay)
    line(Ax, Ay, Bx, By)
    line(Ax, Ay, Cx, Cy)
    line(Cx, Cy, Dx, Dy)
    line(Cx, Cy, endx, endy)


while True:
    turtle.ht()
    turtle.speed(0)
    turtle.pencolor("aqua")
    turtle.bgcolor("black")
    line(-600, 0, 600, 0)
    time.sleep(10)
    turtle.reset()
