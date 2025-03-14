from tkinter import *
from tkinter import messagebox
import random
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def gen_password():
    password_input.delete(0, END)
    password_list = []

    password_list += [random.choice(letters) for n in range(random.randint(8, 10))]
    password_list += [random.choice(numbers) for n in range(random.randint(2, 4))]
    password_list += [random.choice(symbols) for n in range(random.randint(2, 4))]

    random.shuffle(password_list)
    new_password = ''.join(password_list)
    password_input.insert(0, new_password)
    pyperclip.copy(new_password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    with open('passwords.txt', 'a') as file:
        web_input_text = website_input.get()
        user_input_text = username_input.get()
        pass_input_text = password_input.get()
        if len(web_input_text) or len(user_input_text) or len(pass_input_text) == 0:
            messagebox.showinfo(title="Missing Info",message="Please don't leave any information blank")
        else:
            is_ok = messagebox.askokcancel(title=f"Website: {web_input_text}", message=f"Is this info correct?\nUsername: {user_input_text}\nPassword: {pass_input_text}\n")

            if is_ok:
                file.write(f"{web_input_text} | {user_input_text} | {pass_input_text}\n")
                website_input.delete(0, END)
                website_input.focus()
                password_input.delete(0, END)



# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.config(pady=20, padx=20)
window.title("Password Manager")

canvas = Canvas(width=200, height=200, highlightthickness=0)
photo = PhotoImage(file="logo.png")
canvas.create_image(100,100, image=photo)
canvas.grid(column=1, row=0)

website_text = Label(text="Website:", )
website_text.grid(column=0, row=1, sticky='e')

website_input = Entry()
website_input.grid(column=1, row=1, columnspan=2,sticky='we',padx=(10,0), pady = 10)
website_input.focus()

username_text = Label(text="Username/Email:", )
username_text.grid(column=0, row=2, sticky='e')


username_input = Entry()
username_input.grid(column=1, row=2, columnspan=2,sticky='we', padx=(10,0), pady = 10)
username_input.insert(0, "mattbaileywork@gmail.com")

password_text = Label(text="Password:")
password_text.grid(column=0, row=3, sticky='e')

password_input = Entry(width=35)
password_input.grid(column=1, row=3, columnspan=2, sticky='w', padx=(10,0))

gen_pass_button = Button(text="Generate Password", command=gen_password)
gen_pass_button.grid(column=2, row=3, sticky='e', pady = 10)

add_button = Button(text="Add", width=46, command=save_password)
add_button.grid(column=1, row=4, columnspan=2, sticky='we', padx=(9,0), pady = 10)


window.mainloop()