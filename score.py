from turtle import Turtle
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.scr=0
        self.color("white")
        self.penup()
        self.goto(0,260)
        self.write(f"Score: {self.scr}", align='center', font=('Bodoni MT Black', 15, 'normal'))
        self.hideturtle()

    def Fresh_Score(self):
        self.scr+=1
        self.clear()
        self.goto(0,260)
        self.write(f"Score: {self.scr}", align='center', font=('Arial Black', 15, 'normal'))
        self.hideturtle()

    def Game_Over(self):
        self.goto(0,0)
        self.write(f"GAME OVER", align='center', font=('Arial Black', 15, 'normal'))
        self.hideturtle()


