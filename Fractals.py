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
    fifthx = fullx/5
    fifthy = fully/5
    Ax = startx+fifthx
    Ay = starty+fifthy
    Dx = startx+fifthx*2
    Dy = starty+fifthy*2
    Ex = endx-fifthx*2
    Ey = endy-fifthy*2
    Hx = endx-fifthx
    Hy = endy-fifthy
    Bx = Ax-fifthy
    By = Ay+fifthx
    Cx = Dx-fifthy
    Cy = Dy+fifthx
    Fx = Ex+fifthy
    Fy = Ey-fifthx
    Gx = Hx+fifthy
    Gy = Hy-fifthx
    line(startx,starty, Ax,Ay)
    line(Ax,Ay, Bx,By)
    line(Bx,By, Cx,Cy)
    line(Cx,Cy, Dx,Dy)
    line(Dx,Dy, Ex,Ey)
    line(Ex,Ey, Fx,Fy)
    line(Fx,Fy, Gx,Gy)
    line(Gx,Gy, Hx,Hy)
    line(Hx,Hy, endx,endy)

while True:
    turtle.ht()
    turtle.speed(0)
    turtle.pencolor("aqua")
    turtle.bgcolor("black")
    line(-600,0,600,0)
    time.sleep(10)
    turtle.reset()
