import turtle
import math
i = 600
turtle.pu()
turtle.ht()
turtle.left(45)
turtle.forward((math.sqrt(2*i*i)/2))
turtle.right(90)
for x in range(100):
    turtle.right(45)
    if x%2==0:
        turtle.color("black")
    else:
        turtle.color("white")
    turtle.pd()
    turtle.begin_fill()
    for y in range(4):
        turtle.forward(i)
        turtle.right(90)
    turtle.end_fill()
    turtle.pu()
    turtle.forward(i/2)
    i = math.sqrt(2*i*i)/2
    
