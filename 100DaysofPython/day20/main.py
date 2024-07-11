from turtle import Turtle, Screen
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')  # background color
screen.title("My snake game")
screen.tracer(0)

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
    screen.update()  # each update moves
    time.sleep(0.2)  # 1 second delay
    for seg_num in range(len(segments)-1, 0, -1):
        new_x = segments[seg_num - 1].xcor()
        new_y = segments[seg_num - 1].ycor()
        segments[seg_num].goto(new_x, new_y)
    segments[0].forward(20)


screen.exitonclick()

