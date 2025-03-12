from turtle import Turtle
import pandas
from pandas.core.interchange.dataframe_protocol import DataFrame


class States(Turtle):
    def __init__(self):
        super().__init__()
        self.state_info = pandas.read_csv("50_states.csv")
        self.hideturtle()
        self.guess_count = 0
        self.all_states = self.state_info.state.to_list()
        self.guess_states = []

        print(self.all_states)

    def show_state(self, state_guess):
        # asdf = self.state_info[self.state_info.state == state_guess]
        if state_guess in self.all_states:
            state = Turtle()
            state.hideturtle()
            state.penup()
            # x_value = int(asdf.iloc[0, 1])
            # y_value = int(asdf.iloc[0, 2])
            # state.goto(x_value, y_value)
            # state.write(asdf.iloc[0, 0], font=('Arial', 8, 'normal'))
            state_data = self.state_info[self.state_info.state == state_guess]
            state.goto(state_data.x.item(), state_data.y.item())
            state.write(state_guess, font=('Arial', 8, 'normal'))
            self.guess_states.append(state_guess)
        else:
            self.guess_count += 1

        # find_state = self.state_info[self.state_info.state == state_guess]
        #
        # print(find_state)

    def write_missing_states(self):
        missed_states_list = [state for state in self.all_states if state not in self.guess_states]
        df = pandas.DataFrame(missed_states_list)
        print(missed_states_list)
        df.to_csv('missed_states.csv')




