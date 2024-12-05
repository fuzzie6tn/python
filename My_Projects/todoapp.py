from tkinter import *
from tkinter import font

window = Tk()
window.title("To-Do list")
window.config(padx=50, pady=50,bg="pink")
window.geometry("600x600")
fonts= font.families()
custom_font = font.Font(family="FreeMono", size=45)

# Title
title = Label(text="The TODO List", fg="brown", bg="pink", font=(custom_font))
title.config(pady=50)
title.grid(column=0, row=0, columnspan=5)

# enter the task text
enter_the_task= Label(text="Enter the Task:", font=("Courier", 15, "bold"), bg="pink")
enter_the_task.grid(column=0, row=1)

# input
input_task = Entry(width=23)
input_task.grid(column=0,row=2,pady=10)

add_button = Button(text="Add Task",width=20)
add_button.grid(column=0,row=3,pady=10)

delete_button = Button(text="Delete Task",width=20)
delete_button.grid(column=0,row=4,pady=10)

delete_all = Button(text="Delete All",width=20)
delete_all.grid(column=0,row=5,pady=10)

exit_button = Button(text="Exit",width=20)
exit_button.grid(column=0,row=6,pady=10)

window.mainloop()