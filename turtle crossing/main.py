import time, random, threading
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

cars= CarManager()
player = Player()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move_turt, "w")


game_is_on = True
while game_is_on:
    speed = 0.1
    time.sleep(speed)
    screen.update()
    cars.move_car()
    cars.create_cars()

    for car in cars.cars:
        if player.distance(car) <22:
            scoreboard.game_over()
            game_is_on = False

    if player.ycor() >= 260:
        scoreboard.next_level()
        player.reset_turt()
        cars.increase_speed()

    if scoreboard.level == 5:
        scoreboard.game_win()
        game_is_on = False



screen.exitonclick()
