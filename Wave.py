import turtle as tur
import time
while True:
  tur.color("lime")
  tur.bgcolor("black")
  tur.ht()
  tur.pu()
  tur.width(10)
  tur.speed(0)
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
  tur.reset()
