# https://youtu.be/jRk9JKZ2WEE

import turtle
import math
import time
turtle.bgcolor("black")
turtle.ht()
while True:
    i = 600
    turtle.pu()
    turtle.seth(45)
    turtle.forward((math.sqrt(2)*i/2))
    turtle.right(90)
    for x in range(16):
        turtle.right(45)
        turtle.pd()
        if x == 0:
            turtle.color("white", "black")
        elif x % 2 == 0:
            turtle.color("black")
        else:
            turtle.color("white")
        turtle.begin_fill()
        for y in range(4):
            turtle.forward(i)
            turtle.right(90)
        turtle.end_fill()
        turtle.pu()
        turtle.forward(i/2)
        i = math.sqrt(2*i*i)/2
    time.sleep(10)
    turtle.goto(0, 0)
    turtle.clear()
