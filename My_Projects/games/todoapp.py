from tkinter import *
from tkinter import font, messagebox

def add_task():
    task = input_task.get()
    if task.strip():
        list_box.insert(END, task)
        input_task.delete(0,END)
    else:
        messagebox.showwarning(title="Empty", message="Input error, empty task")


def delete_task():
    # select the particular task and press delete_task to delete it


def delete_all_task():
    pass

def exit_task():
    pass

window = Tk()
window.title("To-Do list")
window.config(padx=50, pady=50, bg="pink")
window.geometry("600x600")

fonts = font.families()
custom_font = font.Font(family="FreeMono", size=45)


# Title
title = Label(text="The TODO List", fg="brown", bg="pink", font=custom_font)
title.config(pady=50)
title.grid(column=0, row=0, columnspan=3)  # Span across all columns

# Enter the task text
enter_the_task = Label(text="Enter the Task:", font=("Courier", 15, "bold"), bg="pink")
enter_the_task.grid(column=0, row=1, sticky="w")  # Align to the left

# Input
input_task = Entry(width=23)
input_task.grid(column=0, row=2, pady=10, sticky="w")

# Buttons
add_button = Button(text="Add Task", width=20, command=add_task)
add_button.grid(column=0, row=3, pady=10, sticky="w")

delete_button = Button(text="Delete Task", width=20, command=delete_task)
delete_button.grid(column=0, row=4, pady=10, sticky="w")

delete_all = Button(text="Delete All", width=20,command=delete_all_task)
delete_all.grid(column=0, row=5, pady=10, sticky="w")

exit_button = Button(text="Exit", width=20, command=exit_task)
exit_button.grid(column=0, row=6, pady=10, sticky="w")

# Listbox
list_box = Listbox(
    window,                 # Parent widget
    height=10,              # Number of rows visible
    width=30,               # Number of columns (character width)
    bg="white",             # Background color
    activestyle='dotbox',   # Style of the active item
    font="Helvetica",       # Font style
    fg="black"              # Text color
)
list_box.grid(column=1, row=1, rowspan=8, padx=20)  # Span multiple rows to align with buttons

window.mainloop()
