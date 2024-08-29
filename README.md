# oop_API_quiz_project

## Process:

1. create four pages, api.py, main.py, question_model.py, and quiz_brain.py
2. get api from Trivia
3. connect python with api and retrive data
4. create Question class based in questions listed in api.py in question_model.py
4. in the main.py create question_bank (list of questions)
5. in quiz_brain.py create QuizBrain class
6. bring "quiz" in main.py based on QuizBrain class
7. in the quiz_brain.py create first function-next_question()-when the order number is growing the question will move to the next one
8. create another function-still_has_question()-the number of questions in the list is more than question order number, then it is true, then it should keep running
9. back in the main.py, if still_has_question() is true, then should run next_question()
10. come to the quiz_brain.py to check answers, create check_answer(), if user_answer and correct_asnwer are same, then it is correct
11. add points in check_answer() and still_has_question() when do not have any questions left
