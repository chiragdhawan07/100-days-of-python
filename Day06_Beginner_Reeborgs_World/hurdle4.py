# Day 6 – Beginner – Reeborg's World Hurdle 4 Challenge
# Hurdles of variable height

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    # Climb up the hurdle
    turn_left()
    while wall_on_right():   # climb until there's space to the right
        move()
    # Turn right, cross the hurdle
    turn_right()
    move()
    # Turn right again, move down until ground
    turn_right()
    while front_is_clear():
        move()
    # Face forward again
    turn_left()

# Main loop
while not at_goal():
    if wall_in_front():
        jump()
    else:
        move()
