from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()

        self.window.title("Quizzler")
        self.window.config(background=THEME_COLOR, padx=20, pady=20)

        self.score = Label(text=f"Score: {0}", fg='White', background=THEME_COLOR, font=('Arial', 16))
        self.score.grid(column=1, row=0)

        self.canvas = Canvas(width=300, height=250, background='white', highlightthickness=0)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)
        self.q_text = self.canvas.create_text(150, 125, text='', font=('Arial', 20, 'italic'), fill=THEME_COLOR, justify=CENTER, anchor=CENTER, width=280)

        self.true_image = PhotoImage(file='./images/true.png')
        self.false_image = PhotoImage(file='./images/false.png')
        self.true_button = Button(image=self.true_image, highlightthickness=0)
        self.true_button.grid(column=0, row=2)
        self.false_button = Button(image=self.false_image, highlightthickness=0)
        self.false_button.grid(column=1, row=2)
        self.get_next_question()






        self.window.mainloop()
    def get_next_question(self):
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.q_text, text=q_text)


