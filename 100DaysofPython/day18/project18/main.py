"""Now we'll use the extracted colors
and make a hirst painting using turtle"""

# 10 x 10
# dots should be 20 in size
# spaced or gap between them should be 50

import turtle as turtle_module
from turtle import Screen
import random

turtle_module.colormode(255) # dont forget this part
color_list = [
    (1, 9, 29),
    (121, 96, 42),
    (238, 211, 72), (77, 34, 23),
    (221, 80, 59), (225, 117, 100), (92, 1, 21), (178, 140, 171), (151, 92, 116), (35, 90, 26), (8, 154, 73),
    (204, 64, 92), (220, 178, 219), (167, 129, 76), (1, 63, 146), (4, 220, 218), (3, 80, 30), (80,  35, 178),
    (78, 115, 146), (131, 156, 178), (122, 186, 167), (122, 11, 32), (10, 216, 222), (137, 221, 208), (245, 202, 7),
    (229, 174, 166)
]


tim = turtle_module.Turtle() # object created
tim.speed("fastest")

tim.penup()
tim.hideturtle()
tim.setheading(255)
tim.forward(250)
tim.setheading(0)

number_of_dots = 100
for dot_count in range(1, number_of_dots + 1 ):
    tim.dot(15, random.choice(color_list))
    tim.forward(50)
    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)


screen = Screen()
screen.exitonclick()

