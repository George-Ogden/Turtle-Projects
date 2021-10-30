# https://youtu.be/40q7DRDjf0E

import turtle as tur
import math
import time


def colour(i):
    colours = ["red", "orange", "yellow", "green"]
    try:
        tur.color(colours[i//2])
    except:
        tur.color("blue")


def rotate(origin, point, angle):
    qx = origin[0] + math.cos(angle) * (point[0] - origin[0]) - \
        math.sin(angle) * (point[1] - origin[1])
    qy = origin[1] + math.sin(angle) * (point[0] - origin[0]) + \
        math.cos(angle) * (point[1] - origin[1])
    return [qx, qy]


def line(x, y, x1, y1, x2, y2, angle):
    tur.pu()
    tur.goto(x+x1, y+y1)
    point = rotate([x1, y1], [x2, y2], angle)
    tur.pd()
    tur.goto(x+point[0], y+point[1])


class branch:
    def __init__(self, length, angle, count):
        self.len = length * 2 / 3
        self.ang = angle
        x = tur.xcor()
        y = tur.ycor()
        if self.len > 4:
            colour(count)
            line(x, y, 0, 0, 0, self.len, self.ang+(pi/4))
            count += 1
            branch(self.len, self.ang+(pi/4), count)
            count -= 1
            tur.pu()
            tur.goto(x, y)
            colour(count)
            line(x, y, 0, 0, 0, self.len, self.ang-(pi/4))
            count += 1
            branch(self.len, self.ang-(pi/4), count)
            count -= 1


pi = math.pi
tur.radians()
tur.speed(0)
tur.pensize(2)
tur.ht()
tur.bgcolor("black")
while True:
    tur.color("white")
    tur.pu()
    tur.goto(0, -400)
    tur.pd()
    tur.goto(0, -200)
    branch(300, 0, 0)
    time.sleep(10)
    tur.clear()
