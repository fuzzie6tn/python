import tkinter
from tkinter.ttk import Button

window = tkinter.Tk()
window.title("Gui")
window.configure(background='white')
window.minsize(width=500, height=300)

# label
my_label = tkinter.Label(window, text="Hello World", font=("Calibri", 20, "normal"))
my_label.pack() # this will automatically bring it to the center


def button_clicked():
    my_label.config(text="Button got clicked")
    # print("I got clicked")

button = Button(text = "Click Me", command=button_clicked)
button.pack()
window.mainloop()