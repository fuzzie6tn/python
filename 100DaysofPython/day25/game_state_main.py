import turtle

screen = turtle.Screen()
screen.title("US state game")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

screen.exitonclick()