import time
import turtle
from turtle import forward
from turtle import Screen
from player import Player
from car_manager import CarManager

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.tracer(0) # turned off the tracer


player = Player()
car = CarManager()


screen.listen()
screen.onkey(player.go_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()