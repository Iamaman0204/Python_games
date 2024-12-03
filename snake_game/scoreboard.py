from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.ht()
        self.score = 0
        self.high_score = 0
        f = open("highscore.txt", "r+")
        self.high_score = int(f.read())
        f.close()
        self.pu()
        self.goto(0, 280)
        self.color("green")
        self.update()

    def update(self):
        self.clear()
        self.write(f"Score={self.score},Your HighScore {self.high_score}", move=False, align='center',
                   font=('Arial', 15, 'normal'))

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", move=False, align='center', font=('Arial', 25, 'normal'))

    def reset_t(self):
        if self.score > self.high_score:
            self.high_score = self.score
            f = open('highscore.txt', 'w')
            f.write(str(self.high_score))
            f.close()

        self.score = 0
        self.update()

    def new_score(self):
        self.score += 1
        self.update()
