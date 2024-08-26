from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 190)
        self.write(self.l_score, align="center", font=("Courier", 50, "normal"))
        self.goto(100, 190)
        self.write(self.r_score, align="center", font=("Courier", 50, "normal"))

    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()


class SideSeparation(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.goto(0, -310)
        self.setheading(90)
        self.draw_line()

    def draw_line(self):
        self.pendown()
        self.fd(10)
        self.penup()
        self.fd(10)