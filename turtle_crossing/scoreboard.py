from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self, x=-150, y=250):
        super().__init__()
        self.ht()
        self.score = 1
        self.pu()
        self.goto(x, y)
        self.write(f'Level:{self.score}', align='center', font=FONT)

    def update(self):
        self.clear()
        self.score += 1
        self.write(f'Level:{self.score}', align='center', font=FONT)

    def end_bad(self):
        self.clear()
        self.goto(0, 0)
        self.write("You are Losser", align='center', font=FONT)

    def end_good(self):
        self.clear()
        self.goto(0, 0)
        self.write("You are Winner", align='center', font=FONT)
