from turtle import Turtle, Screen

# import (keyword) turtle (module name)
# import turtle
# tim = turtle.Turtle()

# or

# from(keyword) turtle(module) import(keyword) Turtle(thing in module)
# we can simply write:
# from turtle import Turtle
# tim = Turtle() to create an object


# Let's create an object
tim = Turtle()
tim.shape("turtle")
tim.color("Red")
# making the turtle do something

# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(90)
# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(90)
# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(90)
# timmy_the_turtle.forward(100)

# to make it simple instead of repeating lines of codes
# we will use for loop

for _ in range(4):
    tim.forward(100) # right click, refactor, and then rename
    tim.right(90)




# Window to stay until we click on it and it vanishes, we'll create another object
screen = Screen()
screen.exitonclick()
