import turtle as tur
import time
tur.color("lime")
tur.bgcolor("black")
tur.ht()
tur.width(10)
tur.speed(0)
while True:
  tur.pu()
  tur.goto(-600,100)
  tur.pd()
  delta_1 = 0
  while tur.xcor()<600:
    if tur.ycor() >= 0:
      delta_2 = -10
    else:  
      delta_2 = 10
    delta_1 += delta_2
    tur.goto(tur.xcor() + 8,tur.ycor() + delta_1)
  time.sleep(3)
  tur.clear()
