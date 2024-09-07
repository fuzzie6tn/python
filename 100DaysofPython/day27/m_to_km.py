import tkinter
from tkinter.ttk import Button

from typing_extensions import IntVar

window = tkinter.Tk()
window.title("Mile to Kilo Mile")
window.configure(padx=15, pady=15)
window.minsize(width=150, height=100)

# Entry
mile = tkinter.Entry(width = 10)
mile.grid(row = 0, column = 1)
mile.get()

# Label
text_miles = tkinter.Label(text = "Miles")
text_miles.grid(row = 0, column = 2)

text_2 = tkinter.Label(text = "is equal to")
text_2.grid(row = 1, column = 0)

text_3 =  0
text_3 = tkinter.Label(text = f"{text_3}")
text_3.grid(row = 1, column = 1)

text_4 = tkinter.Label(text = "Km")
text_4.grid(row = 1, column = 2)

#Button





window.mainloop()