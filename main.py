import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
turtle.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    guess_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="Wats`s another states`s name?").title()

    if guess_state == "Exit":
        missing_state = [state for state in all_states if state not in guessed_states]
        mis_state = pandas.DataFrame(missing_state)
        mis_state.to_csv("mis_state.csv")
        break

    if guess_state in all_states and guess_state not in guessed_states:
        guessed_states.append(guess_state)
        t = turtle.Turtle()
        t.penup()
        t.hideturtle()
        state_data = data[data.state == guess_state]
        t.goto(state_data.x.item(), state_data.y.item())
        t.write(guess_state)

