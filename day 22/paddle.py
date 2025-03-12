from turtle import Turtle, Screen
screen = Screen()
RECTANGLE = ((-10, -50), (10, -50), (10, 50), (-10, 50))
screen.register_shape("rectangle", RECTANGLE)


class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.paddles = []
        self.create_paddle()

    def create_paddle(self):
        pad_cord = [(350, 0), (-350, 0)]
        for cord in pad_cord:
            t = Turtle("rectangle")
            t.color('white')
            t.seth(90)
            t.penup()
            t.goto(cord)
            self.paddles.append(t)

    def move_up(self, paddle):
        if paddle.ycor() > 235:
            paddle.goto(paddle.xcor(), paddle.ycor())
        else:
            newy = paddle.ycor() + 20
            paddle.goto(paddle.xcor(), newy)

    def move_down(self, paddle):
        if paddle.ycor() < -235:
            paddle.goto(paddle.xcor(), paddle.ycor())
        else:
            newy = paddle.ycor() - 20
            paddle.goto(paddle.xcor(), newy)