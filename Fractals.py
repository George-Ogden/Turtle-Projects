import turtle as tur
import time, math
def line(startx,starty, endx,endy):
    fullx,fully = endx-startx,endy-starty
    distance = math.sqrt(fully**2+fullx**2)
    if distance < 5:
        tur.pu()
        tur.goto(startx,starty)
        tur.pd()
        tur.goto(endx,endy)
        return
    halfx,halfy = fullx/2,fully/2
    Ax,Ay = halfx+startx,halfy+starty
    Bx,By = Ax-(1/2*(endy-Ay)),1/2*(endx-Ax)+Ay
    line(startx,starty, Ax,Ay)
    line(Ax,Ay, Bx,By)
    line(Bx,By, Ax,Ay)
    line(Ax,Ay, endx,endy)

tur.ht()
tur.speed(0)
tur.color("aqua")
tur.bgcolor("black")
while True:
    line(-600,-200,600,-200)
    time.sleep(10)
    tur.clear()
