# in the beginning there will be a pop-up ask us to bet "who will win the race? enter a color"
# then turtles will line up in the position, and they will start random steps towards the edge of the screen
# soon a turtle will  reach its destination it will print based on the right color
# entered that whether you win or lose
# You lose/win. color turtle is the winner.

# coordinate of x and y-axis is most important in this game.
from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()

screen.setup(width=500, height=400)  # allows the width and height of the screen/window - (keyword arguments)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter the color: ")

colors = ["purple", "blue", "green", "yellow", "orange", "red"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []
#  our turtle is 40 x 40 in size and the end of the edge is 250 to x-axis. so think about it. 250 - (40/2) = 230
for turtle_index in range(0, 6):
    new_turtle = Turtle('turtle')
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:  # if user_bet exists then
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:  # creating random distances for each turtle and moving them forward
        if turtle.xcor()>230:
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print("You Win!")
                is_race_on = False
            else:
                print(f"You Lose! {winning_color} is the winner")
                is_race_on = False
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)


screen.exitonclick()
