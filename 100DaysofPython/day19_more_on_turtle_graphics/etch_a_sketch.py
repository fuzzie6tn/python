# create a turtle
# W key to move forwards
# S key to move backwards
# A key to counter-clockwise / leftwards
# D key to clockwise / rightwards
# C key to clear drawing and put the turtle back in the center
# that will be able to draw things

# MY OWN CODE - YAYYYYYY

"""tim.home()-> move the turtle to the center
   tim.forwards()
   tim.backwards()
   tim.clear()

"""
from turtle import Turtle, Screen

tim = Turtle()


def move_forwards():
    tim.forward(10)


def move_backwards():
    tim.backward(10)


def move_left():
    # tim.left(10)
    new_heading = tim.heading() + 10  # both works the same
    tim.setheading(new_heading)


def move_right():
    # tim.right(10)
    new_heading = tim.heading() - 10  # both works the same
    tim.setheading(new_heading)


def clear_the_sketch():
    tim.penup()
    tim.clear()
    tim.home()
    tim.pendown()


screen = Screen()
screen.listen()

screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=move_left)
screen.onkey(key="d", fun=move_right)
screen.onkey(key="c", fun=clear_the_sketch)

screen.exitonclick()

