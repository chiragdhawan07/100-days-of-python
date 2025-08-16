# Day 6 – Beginner – Reeborg's World Maze Challenge
# Escape using the right-hand rule

def turn_right():
    turn_left()
    turn_left()
    turn_left()

# Maze solving loop
while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()
