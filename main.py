import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

new_cars = []
count = 0
sleep = 0.1

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing Game")
screen.bgcolor("alice blue")
screen.tracer(0)

player = Player()

car_manager = CarManager()
car_manager.hideturtle()

scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.up, "Up")


def update_sleep():
    global sleep
    time.sleep(sleep)


game_is_on = True
while game_is_on:
    update_sleep()
    screen.update()

    # Regenerate a new car every 6th time the loop runs
    count += 1
    if count % 4 == 0:
        car_manager.create_car()
    car_manager.move_cars()

    # Detect when the turtle has reached the top of the screen
    if player.ycor() > 280:
        scoreboard.increase_score()
        player.setpos(0, -280)
        sleep *= 0.5
        update_sleep()

    # Detect if turtle has collided with any of the cars
    for car in car_manager.all_cars:
        if player.distance(car) < 20:
            game_is_on = False
            scoreboard.game_over()
screen.exitonclick()