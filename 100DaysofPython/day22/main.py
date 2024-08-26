from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)  # turns off the animation

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

ball = Ball()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(0.1)  # the ball will move with .1 seconds
    screen.update()  # to turn on the game manually when tracer(0)
    ball.move()

    # detect collision with the wall

    if ball.ycor() > 280 or ball.ycor() < -280:
        # bounce back
        ball.bounce_y()

    # detect collision with paddle
    if ball.distance(r_paddle) < 30 and ball.xcor() > 320 or ball.distance(l_paddle) < 30 and ball.xcor() < -320:
        # bounce back
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.reset_position()

    if ball.xcor() < -380:
        ball.reset_position()


screen.exitonclick()