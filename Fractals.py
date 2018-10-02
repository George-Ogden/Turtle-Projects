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
    rotatex = Ax-(1/2*(endy-Ay))
    rotatey = 1/2*(endx-Ax)+Ay
    Bx = rotatex
    By = rotatey
    line(startx,starty, Ax,Ay)
    line(Ax,Ay, Bx,By)
    line(Bx,By, Ax,Ay)
    line(Ax,Ay, endx,endy)

#line(-240,0,-120,200)
#line(-120,200,120,200)
#line(120,200,240,0)
#line(240,0,120,-200)
#line(120,-200,-120,-200)
#line(-120,-200,-240,0)
##line(-240,0,0,0)
##line(240,0,0,0)
##line(-120,200,0,0)
##line(120,-200,0,0)
##line(-120,-200,0,0)
##line(120,200,0,0)
##line(0,0,240,0)
##line(0,0,-240,0)
##line(0,0,120,-200)
##line(0,0,-120,200)
##line(0,0,-120,-200)
##line(0,0,120,200)
while True:
    turtle.ht()
    turtle.speed(0)
    turtle.pencolor("aqua")
    turtle.bgcolor("black")
    line(-600,-300,600,-300)
    time.sleep(10)
    turtle.reset()
