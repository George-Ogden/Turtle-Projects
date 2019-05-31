import turtle as tur
import math
import time
def hex_col(color):
    return "#" + "".join([str("0"+x[x.find("x")+1:])[-2:] for x in list(map(hex,color))])
def get_col_ang(x,y):
    try:
        theta = math.atan(x/y) * 360 / math.pi
    except:
        theta = 180
    finally:
        return theta
def get_col(theta):
    color = [0,0,0]
    color[int(theta//120)] = int((theta%120)/8*17)
    color[int(theta//120-1)] = int(255-(theta%120)/8*17)
    return hex_col(color)
def circle(angle,radius,pos=(0,0)):
    tur.pu()
    tur.goto(*pos)
    tur.pd()
    tur.seth(angle)
    for i in range(0,360,1):
        tur.color(get_col(get_col_ang(*tur.pos())))
        tur.circle(radius,1)
def major_circle(radius):
    tur.pu()
    tur.goto(0,-radius)
    for i in range(360):
        tur.color(get_col(get_col_ang(*tur.pos())))
        if i*radius/200 % 60 == 0 and (radius != 0 or i == 0):
            for j in range(6):
                circle(j*60,50,tur.pos())
        tur.seth(i)
        tur.circle(radius,1)
while True:
    tur.bgcolor("black")
    tur.speed(0)
    tur.width(5)
    tur.ht()
    for i in range(3):
        major_circle(i*200)
    circle(90,500,(500,0))
    time.sleep(10)
    tur.reset()
    
