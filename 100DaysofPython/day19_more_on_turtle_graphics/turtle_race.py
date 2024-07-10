# in the beginning there will be a pop-up ask us to bet "who will win the race? enter a color"
# then turtles will line up in the position and they will start random steps towards the edge of the screen
# soon a turtle will  reach its destination it will print based on the right color
# entered that whether you win or lose
# You lose/win. color turtle is the winner.

from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400) # allows the width and height of the screen/window - (keyword arguments)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter the color: ")
colors = ["purple", "blue", "green", "yellow", "orange", "red"]
y_positions = [-70, -40, -10, 20, 50, 80]

for turtle_index in range(0, 6):
    tim = Turtle('turtle')
    tim.penup()
    tim.color(colors[turtle_index])
    tim.goto(x=-230, y=y_positions[turtle_index])

if user_bet: # if user_bet exists then
    is_race_on = True

while is_race_on:
    rand_distance = random.randint(0,10)



screen.exitonclick()
