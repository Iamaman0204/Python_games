from turtle import Turtle


class Snake:

    def __init__(self, length):
        self.snake = []
        self.length = length
        self.head = []
        self.new_snake()

    def add_tail(self):
        new_turtle = Turtle()
        new_turtle.pu()
        new_turtle.color("white")
        new_turtle.shape("turtle")
        new_turtle.setpos(self.snake[-1].pos())
        self.snake.append(new_turtle)

    def rightside_turn(self):
        self.head.right(90)

    def leftside_turn(self):
        self.head.left(90)

    def up_turn(self):
        if not self.head.heading() == 270:
            self.head.setheading(90)

    def down_turn(self):
        if not self.head.heading() == 90:
            self.head.setheading(270)

    def right_turn(self):
        if not self.head.heading() == 180:
            self.head.setheading(0)

    def left_turn(self):
        if not self.head.heading() == 0:
            self.head.setheading(180)

    def move_forward(self):
        for i in range(len(self.snake) - 1, 0, -1):
            self.snake[i].goto(self.snake[i - 1].position())
            self.snake[i].setheading(self.snake[i - 1].heading())
        self.head.forward(20)

    def new_snake(self):
        for snake in self.snake:
            snake.ht()
        self.snake.clear()
        self.snake = []
        for i in range(self.length):
            new_turtle = Turtle()
            new_turtle.pu()
            new_turtle.color("white")
            new_turtle.shape("turtle")
            new_turtle.setpos(-i * 20, 0)
            self.snake.append(new_turtle)
        self.head = self.snake[0]
