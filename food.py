from random import randint
from turtle import Turtle
import turtle

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.shapesize(0.8,0.8)
        self.color(randint(0,255),randint(0,255),randint(0,255))
        self.speed("fastest")
        self.location()


    def location(self):
        self.color(randint(0,255),randint(0,255),randint(0,255))
        x=randint(-230,230)
        y=randint(-230,230)
        self.goto(x,y)
        
