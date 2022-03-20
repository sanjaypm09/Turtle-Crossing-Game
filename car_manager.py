from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
Y_POS = [-230, -210, -170, -130, -90, -40, 10, 50, 90, 130, 170, 220]


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.all_cars = []

    def create_car(self):
        x_position = 320
        y_position = random.choice(Y_POS)
        new_car = Turtle(shape="square")
        new_car.pu()
        new_car.color(random.choice(COLORS))
        new_car.shapesize(stretch_wid=1, stretch_len=random.randint(3, 5))
        new_car.setpos(x_position, y_position)
        self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            x = car.xcor() - 10
            y = car.ycor()
            car.setpos(x, y)
