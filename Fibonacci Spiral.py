import turtle as tur
class Fibonacci:
    def __init__(self,max_size):
        self.list = [0,1]
        while self.list[len(self.list)-1] < max_size:
            self.i = self.list[len(self.list)-1] + self.list[len(self.list)-2]
            self.list.append(self.i)
    def main(self,x=0,y=0,square_colour="blue",arc_colour="red"):
        self.square(square_colour,x,y)
        self.arc(arc_colour,x,y)
    def square(self,colour,x=0,y=0):
        tur.pu()
        tur.setx(x)
        tur.sety(y)
        tur.seth(270)
        tur.color(colour)
        tur.pd()
        for i in self.list:
            for j in range(5):
                tur.forward(i)
                tur.right(90)
            tur.forward(i)
    def arc(self,colour,x=0,y=0):
        tur.pu()
        tur.setx(x)
        tur.sety(y)
        tur.seth(90)
        tur.color(colour)
        tur.pd()
        for i in self.list:
            tur.circle(-i,90)
x = -232
y = -143
fibonacci = Fibonacci(500).main(x,y)
#fibonacci.arc(x,y)
