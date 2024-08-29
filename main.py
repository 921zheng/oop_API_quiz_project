from question_model import Question
from quiz_brain import QuizBrain
from api import data

question_bank=[]

for question in data:
    q_text = question["question"]
    q_answer = question["correct_answer"]
    new_question=Question(q_text,q_answer)
    question_bank.append(new_question)

quiz=QuizBrain(question_bank)
while quiz.still_has_question():
    quiz.next_question()
