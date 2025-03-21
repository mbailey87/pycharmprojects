from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = .1
SHORT_BREAK_MIN = .05
LONG_BREAK_MIN = .20

reps = 0
check_count = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- #
def reset_pomodoro():
    global reps,check_count,timer
    window.after_cancel(timer)
    timer_label.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")
    checkmark_label.config(text='')
    reps = 0
    check_count = 0



# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global check_count, reps
    reps += 1
    if reps % 8 == 0:
        countdown(LONG_BREAK_MIN * 60)
        timer_label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        countdown(SHORT_BREAK_MIN * 60)
        timer_label.config(text="Break", fg=PINK)
    else:
        countdown(WORK_MIN * 60)
        timer_label.config(text="Work", fg=GREEN)



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count):
    global check_count

    count_min = math.floor(count/ 60)
    count_sec = count % 60

    if count_sec < 10:
        count_sec = f'0{count_sec}'

    canvas.itemconfig(timer_text, text=f'{count_min}:{count_sec}')

    if count > 0:
        global timer
        timer = window.after(1000, countdown, count - 1)

    else:
        if reps % 2 == 0:
            check_count += 1
            checkmarks()
        start_timer()

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.config(background=YELLOW, padx=100, pady=50)
window.title("Pomodoro")



timer_label = Label(text="Timer", font=(FONT_NAME, 35, "bold"), fg=GREEN, bg=YELLOW, pady=20)
timer_label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, background=YELLOW, highlightthickness=0)
photo = PhotoImage(file="tomato.png")
canvas.create_image(100,112, image=photo)# positions
timer_text = canvas.create_text(100,130, text="00:00", font=(FONT_NAME, 35, "bold"), fill="white")
canvas.grid(column=1, row=1)



start_button = Button(text="Start", font=(FONT_NAME, 10, "bold"), command=start_timer )
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", font=(FONT_NAME, 10, "bold"), command=reset_pomodoro)
reset_button.grid(column=2, row=2)

def checkmarks():
    global check_count

    new_checks = ("✔" * check_count)
    checkmark_label.config(text=new_checks)




checkmark_label = Label(text="", font=(FONT_NAME, 15, "bold"), fg=GREEN, bg=YELLOW, pady=30)
checkmark_label.grid(column=1, row=3)




window.mainloop()