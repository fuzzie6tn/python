from turtle import Screen
import time
from snake import Snake
from food import Food

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')  # background color
screen.title("My snake game")
screen.tracer(0)

snake = Snake()
food = Food()

screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')

# move the snake
game_is_on = True
while game_is_on:
    screen.update()  # each update moves
    time.sleep(0.1)  # 1 second delay
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()

screen.exitonclick()

