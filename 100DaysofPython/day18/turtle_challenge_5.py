# make a spirograph
# 100 distance
# drawing circles
# using random colors

import turtle as t
import random

tim = t.Turtle()
tim.speed("fastest")
t.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

# MY CODE:
# for _ in range(200):
#     tim.color(random_color())
#     tim.circle(100)
#     tim.tilt(50)
#     tim.left(5)


def draw_sprial(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)

draw_sprial(5)


screen = t.Screen()
screen.exitonclick()

