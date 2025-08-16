# Day 6 – Reeborg’s World: Hurdle 3 (Solved)

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

# Keep moving until Reeborg reaches the goal
while not at_goal():
    if wall_in_front():   # jump only when a wall is in front
        jump()
    else:
        move()
