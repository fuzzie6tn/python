from turtle import Turtle, Screen
import time
from snake import Snake
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')  # background color
screen.title("My snake game")
screen.tracer(0)

snake = Snake()

# move the snake
game_is_on = True
while game_is_on:
    screen.update()  # each update moves
    time.sleep(0.1)  # 1 second delayyyyy

    snake.move()
screen.exitonclick()

