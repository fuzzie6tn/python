# draw a random walk, random movemenent of turtle,
# same distance, kept thr color pelatte
# each time it walks it picks a different color
# thickness of the line
# speed up the turtle

import turtle as t
import random
#
colors = ['red', 'SlateGrey', 'SeaGreen', 'green', 'blue', 'violet', 'pink', 'black']
directions = [0, 90, 180, 270]

tim = t.Turtle()
tim.pensize(15)
tim.speed(10)
# to turn it in random direction
for _ in range(200):
    tim.color(random.choice(colors))
    tim.forward(30)
    tim.setheading(random.choice(directions))

# for color_of_turtle in range(200):
#     tim.right(random.randint(0,50))
#     tim.forward(random.randint(0,50))
#     # tim.left(random.randint(0,50))


