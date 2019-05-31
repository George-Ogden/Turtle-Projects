from turtle import *
import time
bgcolor("black")
colour = ["red","yellow","blue","green","purple","dark green","navy blue","pink","orange","cyan","brown","magenta","gold","white"]
ht()
pu()
goto(1000,1000)
time.sleep(10)
goto(0,0)
pd()
speed(0)
while True:
    for i in range(640):
        pensize(1+i/50)
        color(colour[i%(len(colour)-1)])
        forward(50+i)
        left(89)
    time.sleep(10)
    goto(0,0)
    clear()
