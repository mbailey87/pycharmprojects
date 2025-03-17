from operator import index
from tkinter import  *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card={}

# -------------------- CSV info --------------------
try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("data/french_words.csv")



new_dic = data.to_dict(orient='records')
columns = data.columns.tolist()
print(columns)



# -------------------- Functions --------------------

def card_flip():
    global current_card

    canvas.itemconfig(card, image=back_card)
    canvas.itemconfig(word, text=current_card["English"], fill='white')
    canvas.itemconfig(language, text=columns[1], fill='white')


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(new_dic)
    canvas.itemconfig(card, image=front_card)
    canvas.itemconfig(word, text=current_card["French"], fill = 'black')
    canvas.itemconfig(language, text=columns[0],fill = 'black')

    flip_timer = window.after(3000, card_flip)

def known_word():

    new_dic.remove(current_card)
    next_card()
    new_data = pandas.DataFrame(new_dic)
    new_data.to_csv("data/words_to_learn.csv", index=False)

    print(len(new_dic))






# -------------------- UI creation --------------------
window = Tk()
window.title("Flash Cards")
window.config(background=BACKGROUND_COLOR, padx=50,pady=50 )
flip_timer = window.after(3000, card_flip)
front_card = PhotoImage(file='./images/card_front.png')
back_card = PhotoImage(file='./images/card_back.png')
right = PhotoImage(file='./images/right.png')
wrong = PhotoImage(file='./images/wrong.png')

canvas = Canvas(width=800, height=526, highlightthickness=0, background=BACKGROUND_COLOR, )
card = canvas.create_image(400, 263, image=front_card)
language = canvas.create_text(400,100, font=("Arial", 40, 'italic'))
word = canvas.create_text(400,263, font=("Arial", 60, 'bold'))
canvas.grid(column=0, columnspan=2, row=0, pady= (30,10), padx= (30,10))
next_card()

wrong_button = Button(image=wrong, highlightthickness=0, command=next_card)
wrong_button.grid(column=0, row=1, padx=50, )
right_button = Button(image=right, highlightthickness=0, command=known_word)
right_button.grid(column=1, row = 1, padx= 50, )









window.mainloop()