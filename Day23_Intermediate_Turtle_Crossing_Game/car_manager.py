from turtle import Turtle
import random

# Car colors and movement settings
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
SCREEN_RIGHT_EDGE = 360
SCREEN_LEFT_EDGE = -380
Y_BOUNDS = (-250, 250)


class CarManager:
    def __init__(self):
        self.all_cars = []  # active cars on screen
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        # Random chance so cars don't appear every frame
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)  # car shape
            new_car.penup()
            new_car.color(random.choice(COLORS))
            random_y = random.randint(*Y_BOUNDS)
            new_car.goto(SCREEN_RIGHT_EDGE, random_y)
            self.all_cars.append(new_car)

    def move_car(self):
        # Move all cars leftwards
        for car in self.all_cars:
            car.backward(self.car_speed)

        # Remove cars that move off-screen (keeps list clean)
        self.all_cars = [car for car in self.all_cars if car.xcor() > SCREEN_LEFT_EDGE]

    def level_up(self):
        # Increase car speed for next level
        self.car_speed += MOVE_INCREMENT
