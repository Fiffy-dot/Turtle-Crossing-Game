import time
from turtle import Screen
from player import Player
from car_manager import CarManager
import random
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# initialize players, cars, score
player = Player()
car = CarManager()
score = Scoreboard()

game_is_on = True
count = 0  # measures the number of times game loops

# player control
screen.listen()
screen.onkey(player.turtle_up, "Up")

while game_is_on:
    count += 1  # to know where to add cars

    time.sleep(0.1)
    screen.update()

    # generate cars in our game every 6th loop
    if count == 6:
        car.create_car()
        count = 0
    car.move_across()

    # check for turtle collision with cars
    for passing_car in car.all_cars:
        if player.distance(passing_car.pos()) < 25:
            score.game_over()
            game_is_on = False

    # check if turtle player has reached the top edge of the screen and add their score
    if player.player_top_screen():
        player.reset_player()
        score.update_level()
        car.speed_increase()

screen.exitonclick()
