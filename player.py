from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("red4")
        self.pu()
        self.seth(90)
        self.setpos(STARTING_POSITION)

    def up(self):
        self.forward(20)
