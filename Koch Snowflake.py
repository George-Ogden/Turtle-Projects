import turtle as tur
import math
import time

def rotate(origin, point, angle):
    ox = origin[0]
    oy = origin[1]
    px = point[0]
    py = point[1]

    qx = ox + math.cos(angle) * (px - ox) - math.sin(angle) * (py - oy)
    qy = oy + math.sin(angle) * (px - ox) + math.cos(angle) * (py - oy)
    return qx, qy
tur.radians()
tur.speed(0)
  
def line(startx,starty, endx,endy):
    fullx = endx-startx
    fully = endy-starty
    distance = math.sqrt(fully**2+fullx**2)
    if distance < 5:
        tur.penup()
        tur.goto(startx,starty)
        tur.pendown()
        tur.goto(endx,endy)
        return
    thirdx = fullx/ 3
    thirdy = fully/ 3
    Ax = thirdx+startx
    Ay = thirdy+starty
    Cx = 2*thirdx+startx
    Cy = 2*thirdy+starty
    Bx,By = rotate([Ax,Ay],[startx,starty],-math.pi/1.5)
    tur.speed(2)
    line(startx,starty, Ax,Ay)
    line(Ax,Ay, Bx,By)
    line(Bx,By, Cx,Cy)
    line(Cx,Cy, endx,endy)
    
while True:
    length = 140
    tur.ht()
    tur.speed(0)
    tur.pencolor("cyan")
    tur.bgcolor("black")
    line(-length,length*math.sqrt(3), length,length*math.sqrt(3))
    line(length,length*math.sqrt(3), length*2,0)
    line(length*2,0, length,-length*math.sqrt(3))
    line(length,-length*math.sqrt(3), -length,-length*math.sqrt(3))
    line(-length,-length*math.sqrt(3), -length*2,0)
    line(-length*2,0, -length,length*math.sqrt(3))
    time.sleep(10)
    tur.reset()

