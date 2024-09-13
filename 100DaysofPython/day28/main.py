from tkinter import *
import math

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
is_running = False
time_left = 0  # Variable to store remaining time


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps, timer, is_running, time_left
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer", fg=GREEN)
    check_mark_label.config(text="")
    start_button.config(text="Start")
    reps = 0
    is_running = False
    time_left = 0


# ---------------------------- TOGGLE TIMER FUNCTION ------------------------------- #
def toggle_timer():
    global is_running
    if is_running:
        pause_timer()
        start_button.config(text="Start")
    else:
        resume_timer()
        start_button.config(text="Pause")
    is_running = not is_running


# ---------------------------- STOP MECHANISM ------------------------------- #
def pause_timer():
    global timer, time_left
    window.after_cancel(timer)
    title_label.config(text="Paused", fg="blue")


# ---------------------------- RESUME TIMER FUNCTION ------------------------------- #
def resume_timer():
    global time_left

    if time_left > 0:
        count_down(time_left)
    else:
        start_timer()


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps, time_left
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        time_left = long_break_sec
        count_down(long_break_sec)
        title_label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        time_left = short_break_sec
        count_down(short_break_sec)
        title_label.config(text="Break", fg=PINK)
    else:
        time_left = work_sec
        count_down(work_sec)
        title_label.config(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global timer, time_left
    time_left = count

    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")

    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            marks += "✔"
        check_mark_label.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# Label
title_label = Label(text="Timer", font=(FONT_NAME, 35, "bold"), fg=GREEN, bg=YELLOW)
title_label.grid(column=1, row=0)

# Image
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="download.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 133, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"), anchor=CENTER)
canvas.grid(column=1, row=1)

# Buttons
start_button = Button(text="Start", bg="white", command=toggle_timer, highlightthickness=0, borderwidth=0)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", bg="white", highlightthickness=0, borderwidth=0, command=reset_timer)
reset_button.grid(column=2, row=2)

# Checkmark
check_mark_label = Label(font=("Arial", 15, "bold"), fg=GREEN, bg=YELLOW)
check_mark_label.grid(column=1, row=3)

window.mainloop()
