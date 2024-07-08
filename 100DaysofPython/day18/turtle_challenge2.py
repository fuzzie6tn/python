# draw triangle, square, pentagon, hexagon, heptagon, octagon, nonagon and decagon
# three sided shape to 10 sided shapes
# random colors for each shape
# sides should be 100 in terms of length
# shapes overlapped
# consider angles:
# square 90 turn 90 forward 90
# pentagon 72 degree
# 360 / sides to find degree angle

from turtle import Turtle, Screen

tim = Turtle()
tim.shape('turtle')
tim.color('green')

# triangle
for _ in range(3):
    tim.forward(100)
    tim.right(120)

tim.color("grey")

# square

for _ in range(4):
    tim.forward(100)
    tim.right(90)

# pentagon

tim.color("Blue")
for _ in range(5):
    tim.forward(100)
    tim.right(72)
tim.forward(100)

# Hexagon

tim.color("Yellow")
for _ in range(6):
    tim.right(60)
    tim.forward(100)


# heptagon

tim.color("Pink")
for _ in range(7):
    tim.right(51)
    tim.forward(100)

# octagon

tim.color("Orange")
for _ in range(8):
    tim.right(45)
    tim.forward(100)

# nanogon

tim.color("Purple")
for _ in range(9):
    tim.right(40)
    tim.forward(100)

# decagon

tim.color("Black")
for _ in range(10):
    tim.right(36)
    tim.forward(100)

screen = Screen()
screen.exitonclick()
