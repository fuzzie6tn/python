from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import QuizInterface

# this code in creating list of questions stored in question_data
question_bank = [] # empty list
for question in question_data: # goes from each item in question_data list, one by one - each item is stored in quesiton varible
    question_text = question["question"] # extracts the question and stores it in question_text
    question_answer = question["correct_answer"] # same goes here
    new_question = Question(question_text, question_answer) # creating new object of Question class and uses text and answer as inputs
    question_bank.append(new_question) # add kar krhe wahi object ko list mai


quiz = QuizBrain(question_bank)
quiz_ui = QuizInterface(quiz) # new object

# while quiz.still_has_questions():
#     quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
