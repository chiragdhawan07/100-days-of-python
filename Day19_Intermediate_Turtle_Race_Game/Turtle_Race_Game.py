from turtle import Turtle, Screen
import random

# Setup screen
screen = Screen()
screen.title("Turtle Race 🐢🏁")
screen.setup(width=600, height=400)

# Ask for user bet
user_bet = screen.textinput(
    title="Make your bet",
    prompt="Which turtle will win the race? Enter a color (red/blue/orange/green/purple/yellow): "
)

colors = ["red", "blue", "orange", "green", "purple", "yellow"]
y_positions = [130, 80, 30, -20, -70, -120]
all_turtles = []

# Draw finish line
finish_line = Turtle()
finish_line.hideturtle()
finish_line.speed("fastest")
finish_line.penup()
finish_line.goto(250, 150)
finish_line.pendown()
finish_line.right(90)
finish_line.pensize(3)
for _ in range(15):   # dashed line
    finish_line.forward(10)
    finish_line.penup()
    finish_line.forward(10)
    finish_line.pendown()

# Create turtles
for i in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[i])
    new_turtle.goto(x=-270, y=y_positions[i])
    all_turtles.append(new_turtle)

is_game_on = False
if user_bet:
    user_bet = user_bet.lower()
    is_game_on = True

# Race loop
while is_game_on:
    for turtle in all_turtles:
        rand_dist = random.randint(1, 10)
        turtle.forward(rand_dist)

        if turtle.xcor() > 230:
            is_game_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"🎉 You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"😢 You've lost! The {winning_color} turtle is the winner.")

# Exit
screen.exitonclick()
