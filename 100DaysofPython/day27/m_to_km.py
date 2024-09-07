import tkinter
from tkinter.ttk import Button

from typing_extensions import IntVar

window = tkinter.Tk()
window.title("Mile to Kilo Mile")
window.configure(padx=10, pady=10)
window.minsize(width=300, height=200)

# Entry
mile = tkinter.Entry(width = 10)
mile.grid(row = 0, column = 1)
mile.get()


window.mainloop()