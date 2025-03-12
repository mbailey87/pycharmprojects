from turtle import Turtle



class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("highscore.txt") as file:
            current_high_score = file.read()
        self.high_score = int(current_high_score)
        print(self.high_score)
        self.color('white')
        self.penup()
        self.hideturtle()
        self.goto(0,260)
        self.update()

    def update(self):
        self.clear()
        self.write(f'Score: {self.score} High Score: {self.high_score}', align='center', font=('Arial', 24, 'normal'))


    def reset_scoreboard(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open('highscore.txt', mode='w') as score_file:
                score_file.write(str(self.high_score))
        self.score = 0
        self.update()



    # def game_over(self):
    #     self.goto(0,0)
    #     self.write(f'Game Over Your Score: {self.score}', align='center', font=('Arial', 24, 'normal'))

    def increase_score(self):
        self.score += 1

        self.update()