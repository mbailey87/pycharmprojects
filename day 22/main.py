from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time
screen = Screen()
screen.tracer(0)
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title("Pong")
paddle = Paddle()
ball = Ball()
scoreboard = Scoreboard()


r_paddle = paddle.paddles[0]
l_paddle = paddle.paddles[1]
rate_x = ball.rate[0]
rate_y = ball.rate[1]

game_on = True
while game_on:
    screen.update()
    time.sleep(.1)
    screen.listen()
    ball.move_ball()
    if ball.xcor() > 340:
        scoreboard.refresh_l()
        time.sleep(.2)
        ball.new_ball()
    if ball.xcor() < -340:
        scoreboard.refresh_r()
        time.sleep(.2)
        ball.new_ball()

    ball.wall_hit()


    if ball.distance(r_paddle) < 50 and ball.xcor() > 310 or ball.distance(l_paddle) < 50 and ball.xcor() < -310:
        ball.x_change()


    screen.onkey(lambda: paddle.move_up(l_paddle), "w")
    screen.onkey(lambda: paddle.move_down(l_paddle), "s")
    screen.onkey(lambda: paddle.move_up(r_paddle), "Up")
    screen.onkey(lambda: paddle.move_down(r_paddle), "Down")

    if scoreboard.l_score == 7:
        scoreboard.game_over("Left")
        game_on = False
    if scoreboard.r_score == 7:
        scoreboard.game_over("Right")
        game_on = False

screen.exitonclick()