
import turtle
import random

class draw() :
    def __init__(self
                 , num_side : float = 0, size: float = 0, ratio: float = 0, orient: float = 0, border_size: float = 0, color: tuple = (0, 0, 0)):
        import turtle
        turtle.colormode(255)
        self.__num_side = num_side
        self.__ratio = ratio
        self.__size = size
        self.__orient = orient
        self.__location = [0, 0]
        self.__border_size = border_size
        self.__color = color
    @property
    def ratio(self):
        return self.__ratio
    @ratio.setter
    def ratio(self,arg):
        self.__ratio = arg
    @property
    def numside(self):
        return self.__num_side
    @numside.setter
    def numside(self,arg):
        self.__num_side = arg
    @property
    def size(self):
        return self.__size
    @size.setter
    def size(self,arg):
        self.__size = arg
    @property
    def orient(self):
        return self.__orient
    @orient.setter
    def orient(self,arg):
        self.__orient = arg
    @property
    def border_size(self):
        return self.__border_size
    @border_size.setter
    def border_size(self,arg):
        self.__border_size = arg
    @property
    def location(self):
        return self.__location
    @location.setter
    def location(self,arg1):
        self.__location = arg1
    @property
    def color(self):
        return self.__color
    @color.setter
    def color(self,newcolor):
        self.__color = newcolor

    def draw_polygon(self):
        turtle.speed(0)
        turtle.bgcolor('black')
        turtle.tracer(0)
        turtle.penup()
        turtle.goto(self.location[0], self.location[1])
        turtle.setheading(self.orient)
        turtle.color(self.color)
        turtle.pensize(int(self.border_size))
        turtle.pendown()
        for _ in range(int(self.numside)):
            turtle.forward(self.size)
            turtle.left(360/int(self.numside))
        turtle.penup()
class drawrandom(draw):
    def __init__(self):
        super().__init__()
        self.crr = None
    def choice(self):
        self.crr = int(input('select 1-9:  '))
    def randomvariable(self):
        self.numside = random.randint(3, 5)
        self.size = random.randint(50, 150)
        self.orient = random.randint(0, 90)
        self.location = [random.randint(-300, 300), random.randint(-200, 200)]
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.border_size = random.randint(1, 10)
        self.ratio = 0.618
    def reposition(self):
        turtle.penup()
        turtle.forward(self.size*(1-self.ratio)/2)
        turtle.left(90)
        turtle.forward(self.size*(1-self.ratio)/2)
        turtle.right(90)
        self.location[0] = turtle.pos()[0]
        self.location[1] = turtle.pos()[1]
        self.size *= self.ratio
    def drawinside(self):
        self.draw_polygon()
        self.reposition()
    def run(self):
        self.choice()
        self.randomvariable()
        if self.crr == 1:
            for i in range(0,20) :
                self.numside = 3
                for j in range(0,3) :
                    self.draw_polygon()
                self.randomvariable()
            turtle.done()
        elif self.crr == 2 :
            for i in range(0,20) :
                self.numside = 4
                for j in range(0,3) :
                    self.draw_polygon()
                self.randomvariable()
            turtle.done()
        elif self.crr == 3 :
            for i in range(0,20) :
                self.numside = 5
                for j in range(0,3) :
                    self.draw_polygon()
                self.randomvariable()
            turtle.done()
        elif self.crr == 4 :
            for i in range(0,20) :
                for j in range(0,3) :
                    self.draw_polygon()
                self.randomvariable()
            turtle.done()
        elif self.crr == 5 :
            for i in range(0,20) :
                self.numside = 3
                for j in range(0,3) :
                    self.drawinside()
                self.randomvariable()
            turtle.done()
        elif self.crr == 6 :
            for i in range(0,20) :
                self.numside = 4
                for j in range(0,3) :
                    self.drawinside()
                self.randomvariable()
            turtle.done()
        elif self.crr == 7 :
            for i in range(0,20) :
                self.numside = 5
                for j in range(0,3) :
                    self.drawinside()
                self.randomvariable()
            turtle.done()
        elif self.crr == 8 :
            for i in range(0,20) :
                for j in range(0,3) :
                    self.drawinside()
                self.randomvariable()
            turtle.done()
        elif self.crr == 9 :
            for i in range(0,20) :
                p = random.randint(0,1)
                if p == 0 :
                    for j in range(0,3) :
                        self.drawinside()
                else :
                    self.draw_polygon()
                self.randomvariable()
            turtle.done()


a = drawrandom()
a.run()
