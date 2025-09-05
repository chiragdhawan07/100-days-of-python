from turtle import Turtle

class Paddle(Turtle):
    MOVE_DISTANCE = 20
    UPPER_LIMIT = 250
    LOWER_LIMIT = -250

    def __init__(self, position):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)

    def up(self):
        if self.ycor() < self.UPPER_LIMIT:
            new_y = self.ycor() + self.MOVE_DISTANCE
            self.goto(self.xcor(), new_y)

    def down(self):
        if self.ycor() > self.LOWER_LIMIT:
            new_y = self.ycor() - self.MOVE_DISTANCE
            self.goto(self.xcor(), new_y)
