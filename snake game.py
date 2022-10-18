from snake import Snake
from turtle  import Turtle, Screen
from food import Food
from slevel import Level
import time
from score import Score
scr=Screen()
scr.colormode(255)
scr.setup(600,600)
scr.bgcolor("black")
scr.title("Snake Ganme")
scr.listen()
scr.tracer(0)
score=Score()
boundry=Level()
snake=Snake()
scr.listen()
scr.onkey(snake.up,"Up")
scr.onkey(snake.down,"Down")
scr.onkey(snake.left,"Left")
scr.onkey(snake.right,"Right")
tru=True
food=Food()
while tru:
    scr.update()
    time.sleep(0.08)
    snake.move()
    if snake.head.distance(food)<15:
        food.location()
        snake.extend()
        score.Fresh_Score()

    if snake.head.xcor()>=280 or snake.head.ycor()>=245 or snake.head.xcor()<=-280 or snake.head.ycor()<=-245:
        tru=False
        score.Game_Over()
        
    for segment in snake.snk[1:]:
        if snake.head.distance(segment)<10:
            tru=False
            score.Game_Over()
    





scr.exitonclick() 