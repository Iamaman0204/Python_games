import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    def __init__(self):
        self.cars = []

    def car_generator(self):
        if (random.randint(0, 7)) > 5:
            new_car = Turtle()
            new_car.shape("square")
            new_car.shapesize(stretch_len=2, stretch_wid=1)
            new_car.color(random.choice(COLORS))
            new_car.pu()
            new_car.setheading(180)
            new_car.goto(300, random.randint(-10, 10) * 20)
            self.cars.append(new_car)

    def move_car(self):
        for car in self.cars:
            car.forward(STARTING_MOVE_DISTANCE)
        for car in self.cars:
            if car.xcor() < -320:
                car.hideturtle()
                self.cars.remove(car)
                del car

    def collide(self, turtle):
        for car in self.cars:
            if car.distance(turtle) < 20:
                return True
        return False
