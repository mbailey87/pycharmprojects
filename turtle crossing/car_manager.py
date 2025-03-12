from operator import index
from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.cars = []
        self.hideturtle()
        self.movement = STARTING_MOVE_DISTANCE

    def create_cars(self):
        ran_num = random.randint(1,6)
        if ran_num == 1:
            new_car = Turtle("square")
            new_car.shapesize(1, 2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            ran_y = random.randrange(-240, 240, 40)
            new_car.goto(320, ran_y)
            self.cars.append(new_car)

    def move_car(self):
        for i, car in enumerate(self.cars):

            if car.xcor() < -320:
                car.clear()
                car.hideturtle()
                del self.cars[i]

            else:
                car.backward(self.movement)

    def increase_speed(self):
        self.movement += MOVE_INCREMENT