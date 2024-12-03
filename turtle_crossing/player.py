STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
from turtle import Turtle


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.speed_num = 0.2
        self.pu()
        self.setheading(90)
        self.goto(STARTING_POSITION)
        self.shape("turtle")

    def move_up(self):
        self.forward(MOVE_DISTANCE)

    def finished(self):
        return self.ycor() >= FINISH_LINE_Y

    def restart(self):
        self.setheading(90)
        self.goto(STARTING_POSITION)
        self.speed_num *= 0.5
