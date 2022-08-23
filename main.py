from turtle import Turtle, Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

def border():
    border=Turtle()
    border.hideturtle()
    border.speed("fastest")
    border.color("white")
    border.penup()
    border.goto(-300,300)
    border.pendown()
    border.setheading(270)
    border.goto(-300,-300)

    border.setheading(0)
    border.goto(300,-300)

    border.setheading(90)
    border.goto(300,300)

    border.setheading(180)
    border.goto(-300,300)



screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)


snake = Snake()
food=Food()
score=Scoreboard()

game_is_on = True

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.right,"Right")
screen.onkey(snake.left,"Left")
border()
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #Detect collision with food
    if snake.head.distance(food)<15:
        food.refresh()
        snake.extend()
        score.increase_score()

    #Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() <-280:
        game_is_on = False
        score.game_over()

    #Detect collision with tail.
    for segment in snake.segments[1:]:
        if snake.head.distance(segment)<10:
            game_is_on=False
            score.game_over()


screen.exitonclick()