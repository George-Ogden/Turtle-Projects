import turtle as tur
import time, math
def line(startx,starty, endx,endy):
    fullx = endx-startx
    fully = endy-starty
    distance = math.sqrt(fully**2+fullx**2)
    if distance < 5:
        tur.pu()
        tur.goto(startx,starty)
        tur.pd()
        tur.goto(endx,endy)
        return
    halfx = fullx/2
	halfy = fully/2
    Ax = halfx+startx
	Ay = halfy+starty
    Bx = Ax-1/2*(endy-Ay)
	By = 1/2*(endx-Ax)+Ay
    line(startx,starty, Ax,Ay)
    line(Ax,Ay, Bx,By)
    line(Bx,By, Ax,Ay)
    line(Ax,Ay, endx,endy)

tur.ht()
tur.speed(0)
tur.color("aqua")
tur.bgcolor("black")
tur.pu()
while True:
    line(-600,-200,600,-200)
    time.sleep(10)
    tur.clear()
