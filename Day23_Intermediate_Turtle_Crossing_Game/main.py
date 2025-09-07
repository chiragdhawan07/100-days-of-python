import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# Screen setup
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
COLLISION_DISTANCE = 25  # adjusted for stretched cars

screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.tracer(0)

# Game objects
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

# Controls
screen.listen()
screen.onkey(player.go_up, "Up")

# Game loop
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_car()

    # Detect collision with a car
    for car in car_manager.all_cars:
        if car.distance(player) < COLLISION_DISTANCE:
            game_is_on = False
            scoreboard.game_over()

    # Detect successful crossing
    if player.at_finish_line():
        player.go_to_start()
        car_manager.level_up()
        scoreboard.increase_level()

screen.exitonclick()
