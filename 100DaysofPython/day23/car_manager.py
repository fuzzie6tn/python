from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "violet"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []

class CarManager:
    def __init__(self):
        super().__init__()
        for turtle_index in range(0, 6):
            new_turtle = Turtle('square')
            new_turtle.width(10)
            new_turtle.penup()
            new_turtle.color(COLORS[turtle_index])
            new_turtle.goto(x=280, y=y_positions[turtle_index])
            all_turtles.append(new_turtle)
