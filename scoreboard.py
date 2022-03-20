from turtle import Turtle

FONT = ("Courier", 20, "normal")
SCORE_COORD = (-280, 260)


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.pu()
        self.color("black")
        self.setpos(SCORE_COORD)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.clear()
        self.setpos(SCORE_COORD)
        self.write(f"Score:{self.score}", align="left", font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_score()

    def game_over(self):
        self.clear()
        self.color("red")
        self.setpos(0, 0)
        self.write(f"Game Over!", align="center", font=("Courier", 60, "bold"))

