from turtle import Turtle

FONT = ('Courier', 10, 'normal')
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.level = 1
        self.penup()
        self.color('white')
        self.goto(-278, 278)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Level: {self.level} ", align='left', font=FONT)

    def increase_level(self):
        self.level += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.hideturtle()
        self.color("white")
        self.penup()
        self.write('GAME OVER', align='center', font=FONT)