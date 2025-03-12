import time
import turtle
from turtle import Screen
import time

import pandas

from states import States

screen = Screen()
img = 'blank_states_img.gif'

screen.addshape(img)
turtle.shape(img)
STATES = States()
screen.tracer(0)
state_info = STATES.state_info
# print(state_info)
utah = state_info[state_info.state == 'Utah']
# print(utah)

game_on = True
guess_num = 0
while game_on:
    screen.update()
    time.sleep(.1)
    guess = screen.textinput("Guess State", "Guess a state.").title()


    STATES.show_state(guess)



    if STATES.guess_count == 3:
        game_on = False


STATES.write_missing_states()



test = pandas.read_csv('missed_states.csv')
print(test)




















screen.exitonclick()