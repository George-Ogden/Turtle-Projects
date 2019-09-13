import turtle as tur
import math, time

def rotate(origin, point, angle):
    qx = origin[0] + math.cos(angle) * (point[0] - origin[0]) - math.sin(angle) * (point[1] - origin[1])
    qy = origin[1] + math.sin(angle) * (point[0] - origin[0]) + math.cos(angle) * (point[1] - origin[1])
    return qx, qy
  
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
    thirdx = fullx/ 3
    thirdy = fully/ 3
    Ax = thirdx+startx
    Ay = thirdy+starty
    Cx = 2*thirdx+startx
    Cy = 2*thirdy+starty
    Bx,By = rotate([Ax,Ay],[startx,starty],-math.pi/1.5)
    line(startx,starty, Ax,Ay)
    line(Ax,Ay, Bx,By)
    line(Bx,By, Cx,Cy)
    line(Cx,Cy, endx,endy)

length = 400
while True:
    tur.ht()
    tur.speed(0)
    tur.color("cyan")
    tur.bgcolor("black")
    line(-length,length/2, length,length/2)
    line(length,length/2, 0,-length)
    line(0,-length, -length,length/2)
    time.sleep(10)
    tur.reset()

