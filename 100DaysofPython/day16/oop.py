# import another_module
# print(another_module.another_variable)
import prettytable
# from turtle import Turtle, Screen
# timmy = Turtle() #new object from turtle class  timmy is the object here
# print(timmy) # object printed
# timmy.shape('turtle')
# timmy.color('blue')
# timmy.forward(100)
# timmy.right(90)
# timmy.forward(100)
# timmy.right(90)
# timmy.forward(100)
# timmy.right(90)
# timmy.forward(100)
# my_Screen  = Screen()
# print(my_Screen.exitonclick())
from prettytable import PrettyTable #this is class we got access to it

table = PrettyTable()
# print(table)
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmender"] )
table.add_column("Type", ["Electric", "Water", "Fire"])
print(table)