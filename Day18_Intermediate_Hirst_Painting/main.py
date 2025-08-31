import turtle as t
import random

# Create turtle
jimmy = t.Turtle()
t.colormode(255)

# List of colors to choose from (RGB values)
color_list = [
    (240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136),
    (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184),
    (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149),
    (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50),
    (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89),
    (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64),
    (107, 127, 153), (176, 192, 208), (168, 99, 102)
]

# Position turtle at starting point (bottom-left corner)
jimmy.penup()
jimmy.hideturtle()
jimmy.speed("fastest")
jimmy.setheading(225)
jimmy.forward(300)
jimmy.setheading(0)

# Number of dots to draw
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    jimmy.dot(20, random.choice(color_list))  # draw dot with random color
    jimmy.forward(50)  # space between dots

    # After every 10 dots, move up and back to the left
    if dot_count % 10 == 0:
        jimmy.setheading(90)
        jimmy.forward(50)
        jimmy.setheading(180)
        jimmy.forward(500)
        jimmy.setheading(0)

# Keep window open until click
screen = t.Screen()
screen.exitonclick()
