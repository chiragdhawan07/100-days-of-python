from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard22 import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("My Pong Game")
screen.tracer(0)

r_paddle = Paddle((370, 0))
l_paddle = Paddle((-370, 0))
ball = Ball()
scoreboard = Scoreboard()

# Track keys being held down
keys_pressed = {"w": False, "s": False, "Up": False, "Down": False}

def key_press(key):
    keys_pressed[key] = True

def key_release(key):
    keys_pressed[key] = False

# Key bindings for press and release
screen.listen()
screen.onkeypress(lambda: key_press("w"), "w")
screen.onkeyrelease(lambda: key_release("w"), "w")
screen.onkeypress(lambda: key_press("s"), "s")
screen.onkeyrelease(lambda: key_release("s"), "s")
screen.onkeypress(lambda: key_press("Up"), "Up")
screen.onkeyrelease(lambda: key_release("Up"), "Up")
screen.onkeypress(lambda: key_press("Down"), "Down")
screen.onkeyrelease(lambda: key_release("Down"), "Down")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Continuous paddle movement if keys held
    if keys_pressed["w"]:
        l_paddle.up()
    if keys_pressed["s"]:
        l_paddle.down()
    if keys_pressed["Up"]:
        r_paddle.up()
    if keys_pressed["Down"]:
        r_paddle.down()

    # Wall collision
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Paddle collision
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 340) or \
       (ball.distance(l_paddle) < 50 and ball.xcor() < -340):
        ball.bounce_x()

    # Right paddle miss
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.increase_l_score()

    # Left paddle miss
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.increase_r_score()

    # End game condition (first to 10 points)
    if scoreboard.l_score == 10 or scoreboard.r_score == 10:
        scoreboard.game_over()
        game_is_on = False

screen.exitonclick()
