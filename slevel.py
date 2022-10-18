from turtle import Turtle
class Level(Turtle):
    def __init__(self):
        super().__init__()
        self.Boundry()

    def Boundry(self):
        self.penup()
        self.color("white")
        self.goto(-285,250)
        self.pensize(5)
        self.speed("fastest")
        self.pendown()
        self.shapesize(10)
        self.hideturtle()
        for i in range(0,2):
            self.fd(565)
            self.right(90)
            self.fd(500)
            self.right(90)



