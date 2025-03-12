from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 260


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.penup()
        self.seth(90)
        self.goto(STARTING_POSITION)


    def move_turt(self):
            newy = self.ycor() + 100
            self.goto(0, newy)

    def reset_turt(self):
        self.goto(STARTING_POSITION)