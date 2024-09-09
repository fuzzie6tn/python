from tkinter import *

from nala import color

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    count_down(5)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    canvas.itemconfig(timer_text, text=count)
    if count>0:
        window.after(1000, count_down, count-1)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)
# label
timer_label = Label(text="Timer", font=(FONT_NAME, 35, "bold"), fg=GREEN, bg=YELLOW)
timer_label.grid(column=1, row=0)

# Img
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file = "download.png")
canvas.create_image(100,112, image=tomato_img)
timer_text = canvas.create_text(100,133, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"), anchor=CENTER)
canvas.grid(column=1, row=1)

# Buttons
start_button = Button(text="Start", bg="white", command=start_timer, highlightthickness=0, borderwidth=0)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset",bg="white",highlightthickness=0, borderwidth=0)
reset_button.grid(column=2, row=2)

# Checkmark
check_mark_label = Label(text="✔", font=("Arial", 15, "bold"), fg=GREEN, bg=YELLOW)
check_mark_label.grid(column=1, row=3)

window.mainloop()