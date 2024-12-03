import random
import turtle
from turtle import Turtle, Screen

# pikachu = Turtle()
screen = Screen()

# def move_forward():
#     pikachu.forward(10)
#
#
# def move_backward():
#     pikachu.backward(10)
#
#
# def left_turn():
#     pikachu.left(10)
#
#
# def right_turn():
#     pikachu.right(10)
#
#
# def clear():
#     pikachu.clear()
#     pikachu.pu()
#     pikachu.home()
#     pikachu.pd()
#
#
# screen.listen()
# screen.onkey(key="w", fun=move_forward)
# screen.onkey(key="s", fun=move_backward)
# screen.onkey(key="a", fun=left_turn)
# screen.onkey(key="d", fun=right_turn)
# screen.onkey(key="c", fun=clear)

screen.setup(width=500, height=400)
color_turtle = screen.textinput(title="Bet on the turtle:", prompt="Enter the color of tutle which will win")

turtle_list = []
color_list = ['red', 'green', 'yellow', 'blue', 'black']
for _ in range(5):
    turtle_list.append(Turtle())

for i in range(5):
    turtle_list[i].color(color_list[i])
    turtle_list[i].pu()
    turtle_list[i].shape("turtle")
for i in range(5):
    turtle_list[i].goto(x=-230, y=50 * i - 100)
if color_turtle:
    race_on = True
while race_on:
    for i in turtle_list:
        if i.pos()[0] >= 230:
            race_on = False
            print(f"You won {i.color()[0]}.You bet on {color_turtle}")
            break
        i.forward(random.randint(0, 10))

# pikachu.color(color_turtle)
# pikachu.pu()
# pikachu.goto(x=-230, y=0)

screen.exitonclick()
