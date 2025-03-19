from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.input_timer = self.window.after(3000, self.get_next_question)
        self.window.after_cancel(self.input_timer)

        self.window.title("Quizzler")
        self.window.config(background=THEME_COLOR, padx=20, pady=20)

        self.score = Label(text=f"Score: {self.quiz.score}", fg='White', background=THEME_COLOR, font=('Arial', 16))
        self.score.grid(column=1, row=0)

        self.canvas = Canvas(width=300, height=300, background='white', highlightthickness=0)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)
        self.q_text = self.canvas.create_text(150, 150, text='', font=('Arial', 20, 'italic'), fill=THEME_COLOR, width=290)

        self.true_image = PhotoImage(file='./images/true.png')
        self.false_image = PhotoImage(file='./images/false.png')
        self.true_button = Button(image=self.true_image, highlightthickness=0, command=self.true_pressed)
        self.true_button.grid(column=0, row=2)
        self.false_button = Button(image=self.false_image, highlightthickness=0, command=self.false_pressed)
        self.false_button.grid(column=1, row=2)
        self.get_next_question()






        self.window.mainloop()
    def get_next_question(self):
        self.canvas.config(background='white')
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.q_text, text=q_text)
            self.score.config(text=f"Score: {self.quiz.score}")

        else:
            self.canvas.itemconfig(self.q_text, text="You have reached the end of the quiz")
            self.true_button.config(state='disabled')
            self.false_button.config(state='disabled')


    def false_pressed(self):
        self.window.after_cancel(self.input_timer)
        if self.quiz.check_answer(False):
            self.canvas.config(background='green')
        else:
            self.canvas.config(background='red')


        self.input_timer = self.window.after(500,self.get_next_question)


    def true_pressed(self):
        self.window.after_cancel(self.input_timer)
        if self.quiz.check_answer(True):
            self.canvas.config(background='green')
        else:
            self.canvas.config(background='red')

        self.input_timer = self.window.after(500, self.get_next_question)


