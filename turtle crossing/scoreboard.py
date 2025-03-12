from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.goto(0, 260)
        self.hideturtle()
        self.update()

    def update(self):
        self.write(f"Level: {self.level}", align='center', font=FONT)

    def next_level(self):
        self.level += 1
        self.clear()
        self.update()

    def game_over(self):
        text = Turtle()
        text.hideturtle()
        text.write(f"Game Over", align='center', font=FONT)

    def game_win(self):
        text = Turtle()
        text.hideturtle()
        text.write(f"You Win", align='center', font=FONT)