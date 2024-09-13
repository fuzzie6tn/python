from tkinter import *
import math

from click import command
from docutils.nodes import title_reference
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
reps = 0
timer = ""
paused = False
# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    # check_marks reset
    # 00:00 timer_text
    # title "Timer"
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer")
    check_mark_label.config(text="")
    start_button.config(text="Start")
    global reps
    reps = 0
# ---------------------------- Stop MECHANISM ------------------------------- #
def pause_timer():
    global paused
    if not paused:
        window.after_cancel(timer)
        start_button.config(text="Pause")
        title_label.config(text="Paused", fg="Blue")
# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60


    if reps % 8 == 0:
        count_down(long_break_sec)
        title_label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        title_label.config(text="Break", fg=PINK)
    else:
        count_down(WORK_MIN * 60)
        title_label.config(text="Work", fg=GREEN)



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global paused
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count>0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for i in range(work_sessions):
            marks+="✔"
        check_mark_label.config(text=marks)

    pause_timer()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)
# label
title_label = Label(text="Timer", font=(FONT_NAME, 35, "bold"), fg=GREEN, bg=YELLOW)
title_label.grid(column=1, row=0)

# Img
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file = "download.png")
canvas.create_image(100,112, image=tomato_img)
timer_text = canvas.create_text(100,133, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"), anchor=CENTER)
canvas.grid(column=1, row=1)

# Buttons
start_button = Button(text="Start", bg="white", command=start_timer,highlightthickness=0, borderwidth=0)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset",bg="white",highlightthickness=0, borderwidth=0, command=reset_timer)
reset_button.grid(column=2, row=2)

# Checkmark
check_mark_label = Label(font=("Arial", 15, "bold"), fg=GREEN, bg=YELLOW)
check_mark_label.grid(column=1, row=3)

window.mainloop()