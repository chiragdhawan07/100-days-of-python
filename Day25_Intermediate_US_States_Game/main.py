import turtle
import pandas as pd

# Setup Screen
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# Load Data
data = pd.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(
        title=f"{len(guessed_states)}/50 States Correct",
        prompt="What's another state's name? (or type 'Exit' to quit)"
    )

    if not answer_state:  # Handle cancel/empty input
        continue

    answer_state = answer_state.title()

    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        pd.DataFrame(missing_states).to_csv("states_to_learn.csv")
        break

    if answer_state in all_states and answer_state not in guessed_states:
        guessed_states.append(answer_state)

        # Create a marker for the guessed state
        marker = turtle.Turtle()
        marker.hideturtle()
        marker.penup()
        state_data = data[data.state == answer_state]
        marker.goto(state_data.x.item(), state_data.y.item())
        marker.write(answer_state, align="center", font=("Arial", 10, "normal"))
