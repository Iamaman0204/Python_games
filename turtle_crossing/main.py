import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

player = Player()
car_coming = CarManager()
score = Scoreboard()

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

screen.listen()
screen.onkey(key="Up", fun=player.move_up)

game_is_on = True
for i in range(100):
    car_coming.car_generator()
    car_coming.move_car()

while game_is_on:
    time.sleep(player.speed_num)
    screen.update()
    car_coming.car_generator()
    car_coming.move_car()

    if score.score > 3:
        game_is_on = False
        score.end_good()

    elif player.finished():
        player.restart()
        score.update()

    elif car_coming.collide(player):
        game_is_on = False
        score.end_bad()

screen.exitonclick()
