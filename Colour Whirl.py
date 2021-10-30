# https://youtu.be/KOhffwDtdJk

from turtle import *
import time
bgcolor("black")
colour = ["red", "yellow", "blue", "green", "purple", "dark green",
          "navy blue", "pink", "orange", "cyan", "brown", "magenta", "gold", "white"]
ht()
speed(0)
while True:
    for i in range(640):
        pensize(1+i/50)
        color(colour[i % (len(colour)-1)])
        forward(50+i)
        left(89)
    time.sleep(10)
    goto(0, 0)
    clear()
