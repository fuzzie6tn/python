from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')  # background color
screen.title("My snake game")

# body of snake
starting_position = [(0, 0), (-20, 0), (-40, 0)]
segments = []
for positions in starting_position:
    new_segment = Turtle("square")
    new_segment.penup()
    new_segment.color("white")
    new_segment.goto(positions)
    segments.append(new_segment)

# move the snake
game_is_on = True
while game_is_on:
    for segment in segments:
        segment.forward(20)

screen.exitonclick()

