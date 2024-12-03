import time
from turtle import Turtle, Screen
from scoreboard import Scoreboard
from food import Food
import snake

my_screen = Screen()
my_screen.tracer(0)
my_screen.bgcolor("black")
my_screen.setup(600, 600)
my_screen.title("My Snake Game")
snake = snake.Snake(3)
food = Food()
score = Scoreboard()

start_turtle = Turtle()
start_turtle.pu()
start_turtle.ht()
start_turtle.color("blue")
start_turtle.write(" START SNAKES ", move=False, align="center",
                   font=('Times New Roman', 35, 'normal'))
my_screen.textinput("Snakes", "Press Enter")

start_turtle.clear()
my_screen.listen()
my_screen.onkey(key="a", fun=snake.leftside_turn)
my_screen.onkey(key="d", fun=snake.rightside_turn)
my_screen.onkey(key="Up", fun=snake.up_turn)
my_screen.onkey(key="Down", fun=snake.down_turn)
my_screen.onkey(key="Right", fun=snake.right_turn)
my_screen.onkey(key="Left", fun=snake.left_turn)
my_screen.update()
game_on = True
while game_on:
    snake.move_forward()

    # Detect food by snake
    if snake.snake[0].distance(food) < 15:
        snake.add_tail()
        score.new_score()
        food.refresh()

    # Detect boundary by snake
    if snake.snake[0].xcor() < -280 or snake.snake[0].xcor() > 280 or snake.snake[0].ycor() < -280 or snake.snake[
        0].ycor() > 280:
        score.reset_t()
        snake.new_snake()
        # score.game_over()
        # game_on = False

    # Detect collision between head and tail of snake.
    for part in snake.snake[1:]:
        if part.distance(snake.head) < 10:
            score.reset_t()
            snake.new_snake()
            # score.game_over()
            # game_on = False
            break
    my_screen.update()
    time.sleep(0.1)

my_screen.exitonclick()
