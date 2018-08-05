from turtle import *
bgcolor("black")
colour = ["red","yellow","blue","green","purple","dark green","navy blue","pink","orange","cyan","brown","magenta","gold","white"]
for i in range(0, 10000):
    pensize(1+i/50)
    speed(50+i)
    color(colour[i%(len(colour)-1)])
    forward(50+i)
    left(89)

