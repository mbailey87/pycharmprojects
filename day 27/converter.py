from tkinter import  *

window = Tk()
window.title("Miles to Km")
window.config(padx=20, pady=20)


def calc_km():
    miles_num = float(miles_input.get().strip())
    km = round(miles_num * 1.609, 2)
    km_num.config(text=km)

miles_label = Label(text='Miles')
miles_label.grid(column= 2, row=0)

miles_input = Entry(width=5)

miles_input.grid(column= 1, row=0)

equal_label = Label(text='Is Equal To')
equal_label.grid(column= 0, row=1)

km_num = Label(text='0')
km_num.grid(column= 1, row=1)

km_label = Label(text='Is Equal To')
km_label.grid(column= 2, row=1)

calc_button = Button(text="Calculate", command=calc_km)
calc_button.grid(column= 1, row=2)









window.mainloop()