from turtle import *
import time
bgcolor("black")
colour = ["red","yellow","blue","green","purple","dark green","navy blue","pink","orange","cyan","brown","magenta","gold","white"]
ht()
while True:
    for i in range(0, 720):
        pensize(1+i/50)
        speed(50+i)
        color(colour[i%(len(colour)-1)])
        forward(50+i)
        left(89)
    time.sleep(10)
    goto(0,0)
    clear()
