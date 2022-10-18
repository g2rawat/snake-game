from turtle import Turtle, Screen
POSITIONS=[(0,0),(-20,0),(-40,0)]
UP=90
DOWN=270
LEFT=180
RIGHT=0
class Snake:

    def __init__(self):
        self.snk=[]
        self.Create_Snake()
        self.head=self.snk[0]

    def Create_Snake(self):
        for position in POSITIONS:
            self.add_sqr(position)

    def add_sqr(self,position):
        dim=Turtle("square")
        dim.penup()
        dim.color("yellow")
        dim.goto(position)
        self.snk.append(dim)

    def extend(self):
        self.add_sqr(self.snk[-1].position())

    
    
    def move(self):
        for seg_snk in range(len(self.snk)-1,0,-1):
            x=self.snk[seg_snk-1].xcor()
            y=self.snk[seg_snk-1].ycor()
            self.snk[seg_snk].goto(x,y) 
        self.head.forward(20)

    def up(self):
        if self.head.heading()!=DOWN:
            self.snk[0].setheading(UP) 
    def down(self):
        if self.head.heading()!=UP:
            self.head.setheading(DOWN)
    def right(self):
        if self.head.heading()!=LEFT:
            self.head.setheading(RIGHT)
    def left(self):
        if self.head.heading()!=RIGHT:
            self.head.setheading(LEFT)


    