from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.r_score = 0
        self.l_score = 0
        self.color('white')
        self.penup()
        self.hideturtle()
        self.goto(0, 260)
        self.update()

    def update(self):
        self.write(f'{self.l_score} : Score : {self.r_score}', align='center', font=("Comic Sans MS", 20, 'normal'))

    def game_over(self, winner):
        self.goto(0,0)
        self.write(f'The Winner Is: {winner}', align='center', font=("Comic Sans MS", 20, 'normal'))

    def refresh_l(self):
        self.l_score += 1
        self.clear()
        self.update()

    def refresh_r(self):
        self.r_score += 1
        self.clear()
        self.update()