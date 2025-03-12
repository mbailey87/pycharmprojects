from tkinter import  *

window = Tk()
window.title('My First GUI  Program')
window.minsize(width=500, height=300)

#Lable
my_label = Label(text="I am a label", font=("Arial", 24, "bold"))
my_label.pack()

my_label['text'] = 'New Text'

my_label.config(text= 'New Text 2')

def button_click():
    input_text = input.get()
    my_label.config(text= input_text)

# Button
button = Button(text='Click Me', command=button_click) # command is used for events and it is the name of the function
button.pack()

# Entry
input = Entry(width= 50)
input.insert(END,string='Some starting text')
input.pack()

#creates a text box
text = Text(height=5, width=30)
#puts cursor in textbox
text.focus()
#adds some text to  begine with
text.insert(END, "Some more example text")
# Gets current value in text box starting at the first line 1 and character 0
print(text.get('1.0', END))
text.pack()


def spinbox_use():
    print(spinbox.get())

spinbox = Spinbox(from_=0, to=10, width=10, command=spinbox_use)
spinbox.pack()

def scale_use(value):
    print(value)

scale = Scale(from_=0, to=100, command=scale_use)
scale.pack()

# Check Buttons
def checkbutton_use():
    #prints 1 if on 0 if off
    print(checked_state.get())

#creates a variable to check state
checked_state = IntVar()
checkbutton = Checkbutton(text="IS ON?", variable=checked_state, command=checkbutton_use)
checked_state.get()
checkbutton.pack()


#Radio buttons
def radio_use():
    print(radio_state.get())

radio_state = IntVar()
radiobutton1 = Radiobutton(text='option1', value=1, variable=radio_state, command=radio_use)
radiobutton2 = Radiobutton(text='option1', value=2, variable=radio_state, command=radio_use)
radiobutton1.pack()
radiobutton2.pack()

# Listbox
def listbox_used(event):
    #gets currnet selection from listbox
    print(listbox.get(listbox.curselection()))
listbox = Listbox(height=4)
fruits = ['apple', 'pear', 'orange', 'banana']
for fruit in fruits:
    listbox.insert(fruits.index(fruit), fruit)

listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()

window.mainloop()

