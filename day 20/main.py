from turtle import Screen
from snake import Snake
import time
from food import Food
from score_board import Scoreboard
screen = Screen()


screen.setup(width=600, height=600)
screen.tracer(0)
screen.bgcolor('black')
screen.title("My Snake Game")
snake = Snake()
food = Food()
scoreboard = Scoreboard()
screen.listen()



screen.onkey(lambda: snake.turn_snake(90),"w")
screen.onkey(lambda: snake.turn_snake(180),"a")
screen.onkey(lambda: snake.turn_snake(270),"s")
screen.onkey(lambda: snake.turn_snake(0),"d")


game_is_on = snake.game_on
while game_is_on:
    screen.update()
    time.sleep(.1)
    snake.move()

    #detect collision with food
    if snake.head.distance(food) < 15:
        snake.extend()
        food.create_food()
        scoreboard.increase_score()

    if not snake.end_game():
        scoreboard.reset_scoreboard()
        snake.reset_snake()
        food.reset_food()


























screen.exitonclick()