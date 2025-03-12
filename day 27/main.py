from tkinter import  *

window = Tk()
window.title('My First GUI  Program')
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

def button_click():
    input_text = input.get()
    my_label.config(text= input_text)

#Lable
my_label = Label(text="I am a label", font=("Arial", 24, "bold"))
# my_label.pack() # puts everything in a sudo logical order
# my_label.place(x=100,y=200)# places at top left corner
my_label.grid(column=0, row=0)# this puts it top left cant use grid and pack
my_label.config(padx=10, pady=10)

my_label['text'] = 'New Text'

my_label.config(text= 'New Text 2')

# Button
button = Button(text='Click Me', command=button_click) # command is used for events and it is the name of the function
# button.pack()
button.grid(column=1, row=1)
button.config(padx=10, pady=10)

# Entry
input = Entry(width= 20)
input.insert(END,string='Some starting text')
# input.pack()
input.grid(column=3,row=2)
# input.config(padx=10, pady=10)

new_button = Button(text='New Button', command=button_click)
new_button.grid(column=2, row=0)
new_button.config(padx=10, pady=10)


window.mainloop()