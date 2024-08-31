import turtle
import pandas

screen = turtle.Screen()
screen.title("US state game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed = []


while len(guessed) < 50:
    answer_state = screen.textinput(title = f"{len(guessed)}/50 States Correct",
                                    prompt="What's another state's name?").title()
    print(answer_state)

    if answer_state == "Exit":
        missing_states =  []
        for state in all_states:
            if state not in guessed:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        print(missing_states)
        break
    # If answer_state is one of the states in all the states of the 50_states.csv
    if answer_state in all_states:
        guessed.append(answer_state )
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x.iloc[0]), int(state_data.y.iloc[0]))
        t.write(state_data.state.item()) # error will be coordinates are stored as strings ---- or answer_state
        # If they got it right:
        # Create a turtle to write the name of the state at the state's x and y coordinate

