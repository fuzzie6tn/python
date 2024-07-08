# turtle challenge
# draw dashed line 10 paces, and a gap of 10 paces and a solid line of 10 paces and repeat this 50 times

from turtle import Turtle, Screen
tim = Turtle()
tim.shape('turtle')
tim.color("Green")

for _ in range(10):
    tim.forward(10)
    tim.penup()
    tim.forward(10)
    tim.pendown()


screen = Screen()
screen.exitonclick()

