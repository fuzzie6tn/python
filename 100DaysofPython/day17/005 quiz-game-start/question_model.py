class Question:
    def __init__(self, question_text, correct_answer):
        self.text = question_text
        self.answer = correct_answer

    def __str__(self):
        return self.text
