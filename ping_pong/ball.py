from turtle import Turtle
from random import randint

COLOR = "White"


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.pu()
        self.color(COLOR)
        self.shape("circle")
        self.start(1)
        self.move_speed = 0.1

    def start(self, num):
        # self.setheading(-60)
        self.goto(0, 0)
        self.move_speed = 0.1
        if num == 1:
            self.setheading(num * randint(-45, 45))
        else:
            self.setheading(180 + randint(-45, 45))

    def move(self):
        self.forward(10)
        if abs(self.pos()[1]) > 280:
            self.horizontal_bounce()

    def horizontal_bounce(self):
        self.move_speed *= 0.9
        self.setheading(360 - self.heading())

    def vertical_bounce(self):
        if self.heading() < 90:
            self.setheading(180 - self.heading())
        else:
            self.setheading(540 - self.heading())
