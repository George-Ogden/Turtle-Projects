#Fractals along a line
import time
import math
import turtle
def line(startx,starty, endx,endy):
    fullx = endx-startx
    fully = endy-starty
    distance = math.sqrt(fully**2+fullx**2)
    if distance < 6:
        turtle.penup()
        turtle.goto(startx,starty)
        turtle.pendown()
        turtle.goto(endx,endy)
        return
    halfx = fullx/ 2
    halfy = fully/2
    Ax = halfx+startx
    Ay = halfy+starty
    rotatex = Ax-(1/2*(halfy))
    rotatey = 1/2*(halfx)+Ay
    Bx = rotatex
    By = rotatey
    line(startx,starty, Ax,Ay)
    line(Ax,Ay, Bx,By)
    line(Bx,By, Ax,Ay)
    line(Ax,Ay, endx,endy)

while True:
    turtle.ht()
    turtle.speed(0)
    turtle.pencolor("aqua")
    turtle.bgcolor("black")
    line(-600,-300,600,-300)
    time.sleep(10)
    turtle.reset()
