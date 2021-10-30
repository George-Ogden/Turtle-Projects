# https://youtu.be/VpAzyA4pWz8

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
    quarterx = fullx/4
    quartery = fully/4
    Ax = startx+quarterx
    Ay = starty+quartery
    Mx = startx+quarterx*2
    My = starty+quartery*2
    Fx = endx-quarterx
    Fy = endy-quartery
    Bx = Ax-quartery
    By = Ay+quarterx
    Cx = Mx-quartery
    Cy = My+quarterx
    Dx = Mx+quartery
    Dy = My-quarterx
    Ex = Fx+quartery
    Ey = Fy-quarterx
    line(startx, starty, Ax, Ay)
    line(Ax, Ay, Bx, By)
    line(Bx, By, Cx, Cy)
    line(Cx, Cy, Dx, Dy)
    line(Dx, Dy, Ex, Ey)
    line(Ex, Ey, Fx, Fy)
    line(Fx, Fy, endx, endy)


while True:
    turtle.ht()
    turtle.speed(0)
    turtle.pencolor("aqua")
    turtle.bgcolor("black")
    line(-600, 0, 600, 0)
    time.sleep(10)
    turtle.reset()
