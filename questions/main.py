from question_model import Questions
from data import question_data
from quiz_brain import QuizBrain
from random import randint


question_bank = []
for item in question_data:
    question_bank.append(Questions(item["text"], item["answer"]))


quiz = QuizBrain(question_bank)  # Bir değişkene tutunması gerek !!!!!!!


for x in range(len(question_bank)):
    quiz.next_question()
