import tkinter
from tkinter.ttk import Button

window = tkinter.Tk()
window.title("Gui")
window.configure(background='white')
window.minsize(width=500, height=300)

# label
my_label = tkinter.Label(window, text="Hello World", font=("Calibri", 20, "normal"))
my_label.pack() # this will automatically bring it to the center

# button
def button_clicked():
    new_text = input.get()
    my_label.config(text=new_text)

button = Button(text = "Click Me", command=button_clicked)
button.pack()

# entry
input = tkinter.Entry(width = 10)
input.pack()
input.get()

window.mainloop()
