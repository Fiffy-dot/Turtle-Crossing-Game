from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):

        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE + MOVE_INCREMENT

    def create_car(self):
        new_car = Turtle("square")
        new_car.penup()
        new_car.color(random.choice(COLORS))
        new_car.shapesize(stretch_len=2, stretch_wid=1)
        y_pos = random.randint(-250, 250)
        new_car.goto(x=300, y=y_pos)
        self.all_cars.append(new_car)

    def move_across(self,):
        for car in self.all_cars:
            car.back(STARTING_MOVE_DISTANCE)

    def speed_increase(self):
        for car in self.all_cars:
            car.back(self.car_speed)

        self.car_speed += MOVE_INCREMENT






