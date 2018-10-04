import turtle as tur
import math
import time

rt3 = math.sqrt(3)/2
def triangle(top,length,i=False):
    tx,ty = top[0],top[1]
    if length < 8:
        return
    tur.pu()
    if i:        
        tur.goto(tx,ty)
        tur.color("white")
        tur.pendown()
        tur.begin_fill()
        for i in range(3):
            tur.forward(length)
            tur.right(120)
        tur.end_fill()
    tur.goto(tx-(length/4),ty-(length*rt3/2))
    tur.color("black")
    tur.begin_fill()
    tur.goto(tx+(length/4),ty-(length*rt3/2))
    tur.goto(tx,ty-(length*rt3))
    tur.end_fill()
    triangle([tx,ty],length/2)
    triangle([tx-(length/4),ty-(length*rt3/2)],length/2)
    triangle([tx+(length/4),ty-(length*rt3/2)],length/2)

length = 380
y = (length*rt3)
x = length/2
while True:
    tur.ht()
    tur.seth(-60)
    tur.speed(0)
    tur.color("white")
    tur.bgcolor("black")
    triangle([0,y],length,True)
    triangle([-x,0],length,True)
    triangle([x,0],length,True)
    time.sleep(10)
    tur.reset()
