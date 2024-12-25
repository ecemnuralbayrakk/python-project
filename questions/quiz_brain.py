from pyclbr import Class


class QuizBrain:

    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def check_answer(self, user_answer, correct_answer):
        pass

    def next_question(self):
        if self.question_number < len(self.question_list):
            current_question = self.question_list[self.question_number]  ## değişkene tutulması gerek
            print(f"{current_question.quest}")
            self.question_number = self.question_number +  1

