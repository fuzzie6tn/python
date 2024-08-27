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
car_manager = CarManager()


screen.listen()
screen.onkey(player.go_up, "Up")



game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    # detect collision with the car

    for car in car_manager.all_cars:
        if car.distance(player) < 23:
            game_is_on = False

    # detect if at finish line
    if player.is_at_finish_line():
        player.go_to_start()


screen.exitonclick()