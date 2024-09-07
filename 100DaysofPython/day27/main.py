import tkinter
from tkinter.ttk import Button

from typing_extensions import IntVar

window = tkinter.Tk()
window.title("Gui")
window.configure(padx=10, pady=10)
window.minsize(width=500, height=300)


# label
my_label = tkinter.Label(window, text="Hello World", font=("Calibri", 20, "normal"))
# my_label.pack() # this will automatically bring it to the center
my_label.grid(column=0, row=0)
# button
def button_clicked():
    new_text = input.get()
    my_label.config(text=new_text)

button = Button(text = "Click Me", command=button_clicked)
button.grid(column=1, row=2)

button_2 = Button(text = "Button2", command=button_clicked)
button_2.grid(column=2, row=0)

# entry
input = tkinter.Entry(width = 10)
input.grid(row = 2, column = 2)
input.get()

# spinbox
def spinbox_used():
    print(spinbox.get())

spinbox = tkinter.Spinbox(from_=0, to=100, command=spinbox_used, width=5)


# checkbox
# def checkbutton_used():
#     print(check_state.get())
#
# # check_state = IntVar()
# # checkbutton = tkinter.Checkbutton(text= "is on?", variable=check_state, command= checkbutton_used)
# # check_state.get()
# # checkbutton.pack()
window.mainloop()
