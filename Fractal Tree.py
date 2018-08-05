import turtle as tur
import math
def colour(count):
    if count < 2:
        tur.color("red")
    elif count < 4:
        tur.color("orange")
    elif count < 6:
        tur.color("yellow")
    elif count < 8:
        tur.color("green")
    else:
        tur.color("blue")
def rotate(origin, point, angle):
    ox = origin[0]
    oy = origin[1]
    px = point[0]
    py = point[1]

    qx = ox + math.cos(angle) * (px - ox) - math.sin(angle) * (py - oy)
    qy = oy + math.sin(angle) * (px - ox) + math.cos(angle) * (py - oy)
    return [qx, qy]
tur.radians()
tur.speed(100)
tur.pensize(2)
tur.pu()
tur.goto(0,-400)
tur.pd()
tur.goto(0,-200)
def line(x,y,x1,y1,x2,y2,angle):
  tur.pu()
  tur.goto(x+x1,y+y1)
  point = rotate([x1,y1],[x2,y2], angle)
  tur.pd()
  tur.goto(x+point[0],y+point[1])
class branch:
    def __init__(self,length,angle,count):
        self.length = length * 2 / 3
        self.angle = angle
        self.x = tur.xcor()
        self.y = tur.ycor()
        if self.length > 4:
            colour(count)
            line(self.x,self.y,0,0,0,self.length,self.angle+(math.pi/4))
            count += 1
            branch(self.length,self.angle+(math.pi/4),count)
            count -= 1
            tur.pu()
            tur.goto(self.x,self.y)
            colour(count)
            line(self.x,self.y,0,0,0,self.length,self.angle-(math.pi/4))
            count += 1
            branch(self.length,self.angle-(math.pi/4),count)
            count -= 1
          
branch(300,0,0)
