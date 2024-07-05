class Question:
    def __init__(self, question_text, correct_answer):
        self.text = question_text
        self.answer = correct_answer

new_q = Question("What is this?", "this is something")
print(new_q.text)
print(new_q.answer)

