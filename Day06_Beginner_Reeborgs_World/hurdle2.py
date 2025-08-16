# Day 6 – Reeborg’s World: Hurdle 2 (Solved)

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

# Keep jumping until Reeborg reaches the goal
while not at_goal():
    jump()
