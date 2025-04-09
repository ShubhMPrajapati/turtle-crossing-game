from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(x=-280, y=250)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(arg=f"LEVEL: {self.level}", font=FONT)

    def score_increase(self):
        self.level += 1
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.write(arg=f"GAME OVER!", align="center", font=FONT)
