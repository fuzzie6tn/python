from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quiz_brain:QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk() # sab se pehle window banate hain
        self.window.title("Quizzler") # window ko title dia
        self.window.config(padx=20, pady=20, bg=THEME_COLOR) # config method k zariye ham ne padding of bg color dia

        self.score_label = Label(text="Score: 0",bg=THEME_COLOR, fg="white") # Label banaya (text)
        self.score_label.grid(row=0,column=1) # isko ham ne grid k zariye place kr diya

        self.canvas = Canvas(width=300, height=250, bg= "white") # canvas banaya usko height width di
        self.question_text = self.canvas.create_text(  # canvas k andr text banaya_ create_text() ko use kr k
            150, # ye lazmi hai
            125, # ye bhi lazmi hai
            width=280,
            text="Some Question",
            fill=THEME_COLOR,
            font= ("Arial", 20, "italic")
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50) # canvas ko place kkiya

        true_image = PhotoImage(file="images/true.png") # PhotoImage() ko use kr k photo banya
        self.true_button = Button(image=true_image, highlightthickness=0, command=self.true_pressed) # Button bnaya or or k andr wahi image dala
        self.true_button.grid(row=2, column=0) # grid

        false_image = PhotoImage(file="images/false.png") # false image bnaya
        self.false_button = Button(image=false_image, highlightthickness=0, command=self.false_pressed) # button k andr dala
        self.false_button.grid(row=2, column=1) # gird

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz.")

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)

