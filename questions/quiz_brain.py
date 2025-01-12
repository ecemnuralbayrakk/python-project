from pyclbr import Class


class QuizBrain:

    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def check_answer(self, user_answer, correct_answer):
        if user_answer == correct_answer:
            print("Correct Answer")
        else:
            print("Wrong Answer")

        pass

    def next_question(self):
        if self.question_number < len(self.question_list):
            current_question = self.question_list[
                self.question_number
            ]  ## değişkene tutulması gerek
            user_answer = input(f'{current_question.quest}, "True/False"')
            self.check_answer(user_answer, current_question.answer)
            self.question_number = self.question_number + 1
