from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
question_bank = []

for q in question_data:
    question_text = q["question"]
    question_answer = q["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz_brain = QuizBrain(question_bank)

while quiz_brain.still_has_questions():
    quiz_brain.next_question()

print(f"You have completed the quiz\n"
      f"Your final score was {quiz_brain.score}/{quiz_brain.question_num}")