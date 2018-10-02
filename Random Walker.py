import turtle as tur
import random
import math
while True:
    tur.shape("circle")
    tur.speed(100)
    distance = 20
    tur.bgcolor("black")
    tur.color("white")
    num = random.randint(1,8)
    tur.seth(num * 45)
    if num // 2 == 0:
        tur.forward(distance)
    else:
        tur.forward(math.sqrt(distance*2))
    if abs(tur.xcor())>1000 or abs(tur.ycor())>400:
        tur.reset()
    
