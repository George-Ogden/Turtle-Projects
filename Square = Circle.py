from turtle import *
import time
color('orange')
speed(0)
pensize(1)
bgcolor("black")
ht()
while True:
    for i in range(0, 360):
        forward(225)
        left(90)
        forward(225)
        left(90)
        forward(225)
        left(90)
        forward(225)
        left(90)
        left(1)
    time.sleep(10)
    goto(0,0)
    clear()
        
