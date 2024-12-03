from turtle import Turtle

FONT = ('Arial', 50, 'bold')
ALIGNMENT = "center"


class ScoreBoard(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.speed(10)
        self.color("white")
        self.x = x
        self.y = y
        self.pu()
        self.ht()
        self.score_r = 0
        self.score_l = 0
        self.score_write()

    def update_r(self):
        self.goto(self.x, self.y)
        self.score_r += 1
        self.score_write()

    def update_l(self):
        self.goto(-self.x, self.y)
        self.score_l += 1

        self.score_write()

    def score_write(self):
        self.clear()
        self.goto(self.x, self.y)
        self.write(f"{self.score_r}", move=False, align=ALIGNMENT, font=FONT)

        self.goto(-self.x, self.y)
        self.write(f"{self.score_l}", move=False, align=ALIGNMENT, font=FONT)

    def dash_line(self):
        self.width(10)
        self.pu()
        self.goto(0, 300)
        self.setheading(270)
        for i in range(600 // 50):
            self.pd()
            self.forward(25)
            self.pu()
            self.forward(25)
        self.goto(self.x, self.y)
