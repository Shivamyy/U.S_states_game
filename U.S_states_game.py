import turtle 
import pandas
# turtle=Turtle()
my_screen=turtle.Screen()
my_screen.title("U.S. states Game")
image="blank_states_img.gif"
my_screen.addshape(image)
turtle.shape(image)


correct_guess=[]

data=pandas.read_csv("50_states.csv")
all_states=data.state.to_list()
while len(correct_guess)<50:
    answer_state=my_screen.textinput(title="Guess the state", prompt="What's another state name?").title()
    if answer_state=="Exit":
        missing_states=[]
        for state in all_states:
            if state not in correct_guess:
                missing_states.append(state)
        new_data=pandas.DataFrame(missing_states)
        new_data.to_csv("Missing_states.csv")
        break
    if answer_state in all_states:
        correct_guess.append(answer_state)
        t=turtle.Turtle()
       
        t.hideturtle()
        t.penup()
        state_data=data[data.state==answer_state]
        t.goto(int(state_data.x),int(state_data.y))
        t.write(answer_state)

# states_to_learn.csv
