from turtle import Turtle

# Constants for snake behavior
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
SNAKE_COLOR = "white"
UP, DOWN, LEFT, RIGHT = 90, 270, 180, 0


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    # Create the initial snake with 3 segments.
    def create_snake(self):
        
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    # Add a new segment at the given position.
    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color(SNAKE_COLOR)
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)
        
    # Grow the snake by adding a segment at the tail.
    def extend(self):
        self.add_segment(self.segments[-1].position())

    # Move the snake forward by shifting segments.
    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    # Direction controls
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    # Reset the snake to starting size and position.
    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)  # move old segments off-screen
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]
