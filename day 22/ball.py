from turtle import Turtle
import random



class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.rate = []
        self.create_ball()

    def move_ball(self):

            new_y = self.ycor() + self.rate[1]
            new_x = self.xcor() + self.rate[0]
            self.goto(new_x, new_y)

    def wall_hit(self):
        if self.ycor() >= 230 or self.ycor() <= -230:
            self.y_change()

    def y_change(self):
        self.rate[1] = -self.rate[1]

    def x_change(self):
        self.rate[0] *= -1
        if self.rate[0] > 0:
            self.rate[0] += 5
        else:
            self.rate[0] -= 5

    def create_ball(self):
        self.shape('circle')
        self.color('white')
        self.penup()
        def ran_deg():
            choice = [-1, 1]
            direction = random.choice(choice)
            return direction

        self.rate = [ran_deg()*10, ran_deg()*10]

    def new_ball(self):
        self.reset()
        self.create_ball()



