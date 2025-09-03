from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.update_score()
        self.hideturtle()

    # Update the score display.
    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    # Add a point and update score.
    def increase_score(self):
        self.score += 1
        self.update_score()

    # Display "GAME OVER" at the center.
    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
