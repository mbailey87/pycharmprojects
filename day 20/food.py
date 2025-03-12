from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):

        super().__init__()
        self.shape("circle")
        self.penup()
        self.color('blue')
        self.shapesize(.75, .75)
        self.speed("fastest")
        self.create_food()

    def create_food(self):
        x = random.randrange(-280, 281, 20)
        y = random.randrange(-280, 281, 20)
        self.goto(x, y)

    def reset_food(self):
        self.clear()
        self.create_food()