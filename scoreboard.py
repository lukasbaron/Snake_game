from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Courier', 12, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.setposition(0, 260)
        self.number = 0
        self.score()

    def score(self):
        self.write(f"Score: {self.number}", False, ALIGNMENT, FONT)

    def game_over(self):
        self.setposition(0, 0)
        self.write("GAME OVER",  False, ALIGNMENT, FONT)

    def counter(self):
        self.clear()
        self.number += 1
        self.score()
