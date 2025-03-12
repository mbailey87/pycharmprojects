class QuizBrain:

    def __init__(self, q_list):
        self.question_num = 0
        self.question_list = q_list
        self.score = 0

    def next_question(self):
        correct_answer = self.question_list[self.question_num].answer.lower()
        cur_answer = input(f"Q.{self.question_num+1}: {self.question_list[self.question_num].text} (True or False)\n").lower()
        if cur_answer == correct_answer:
            self.question_num += 1
            print("Correct")
            self.score += 1
            print(f"{self.score}/{self.question_num}")
        else:
            print(f"Incorrect the right answer was {self.question_list[self.question_num].answer}")
            self.question_num += 1
            print(f"{self.score}/{self.question_num}")

    def still_has_questions(self):
        return self.question_num < len(self.question_list)
