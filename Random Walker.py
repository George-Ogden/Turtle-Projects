import turtle as tur
import random
import math
tur.speed(100)
distance = 20
for i in range(1000000):
    num = random.randint(1,8)
    tur.seth(num * 45)
    if num // 2 == 0:
        tur.forward(distance)
    else:
        tur.forward(math.sqrt(distance*2))
