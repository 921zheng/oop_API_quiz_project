class QuizBrain:
    def __init__(self,q_list):
        self.q_list=q_list
        self.q_num=0
        self.point=0

    def still_has_question(self):
        if self.q_num < len(self.q_list):
            return True
        else:
            print(f"all done, your final score is {self.point}/{len(self.q_list)}")


    def next_question(self):
        quiz_shown=self.q_list[self.q_num]
        self.q_num+=1
        user_answer=input (f"Q{self.q_num}: {quiz_shown.q_text}")
        self.check_answer(user_answer,quiz_shown.q_answer)

    def check_answer(self,user_answer,real_answer):

        if user_answer.lower()==real_answer.lower():
            self.point+=1
            print(f"you are right, correct answer is {user_answer}, and your point is {self.point}")
        else:
            print(f"you are wrong, correct answer is {real_answer}, and your point is {self.point}")
