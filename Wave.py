import turtle as tur
import time
tur.color("lime")
tur.bgcolor("black")
tur.ht()
tur.width(10)
tur.speed(0)
while True:
  tur.pu()
  tur.goto(-900,300)
  tur.pd()
  delta_1 = 0
  while tur.xcor()<900:
    if tur.ycor() >= 0:
      delta_2 = -1
    else:  
      delta_2 = 1
    delta_1 += delta_2
    tur.goto(tur.xcor() + 4,tur.ycor() + delta_1)
  time.sleep(2)
  tur.clear()
