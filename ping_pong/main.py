import time

from scoreboard import ScoreBoard
from player import Player
from ball import Ball
from turtle import Screen

screen = Screen()
screen.title("Ping-Pong")
screen.setup(height=600, width=800)
screen.bgcolor("black")
screen.tracer(0)

paddle_one = Player(350, 0)
paddle_two = Player(-350, 0)

ball = Ball()

score = ScoreBoard(40, 180)

screen.listen()
screen.onkey(fun=paddle_one.go_up, key="Up")
screen.onkey(fun=paddle_one.go_down, key="Down")
screen.onkey(fun=paddle_two.go_up, key="w")
screen.onkey(fun=paddle_two.go_down, key="s")
# screen.onkey(fun=player2.move_up, key="w")
# screen.onkey(fun=player2.move_down, key="s")
game_is_on = True
while game_is_on:
    screen.update()
    # time.sleep(ball.move_speed)
    ball.move()
    if ball.distance(paddle_two) < 50 and ball.xcor() < -320 or ball.distance(paddle_one) < 50 and ball.xcor() > 320:
        ball.vertical_bounce()
    elif ball.xcor() > 380:
        score.update_l()
        ball.start(-1)
    elif ball.xcor() < -380:
        score.update_r()
        ball.start(1)

screen.exitonclick()
