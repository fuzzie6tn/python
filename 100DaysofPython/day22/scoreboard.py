from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.lScore = 0
        self.rScore = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-165, 265)
        self.write(self.lScore, align='center', font=('Arial', 16, 'bold'))
        self.goto(165, 265)
        self.write(self.rScore, align='center', font=('Arial', 16, 'bold'))

    def l_point(self):
        self.lScore += 1
        self.update_score()

    def r_point(self):
        self.rScore += 1
        self.update_score()
