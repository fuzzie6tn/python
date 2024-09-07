from tkinter import *

window = Tk()
window.title("Mile to Kilo Mile")
window.configure(padx=15, pady=15)
# window.minsize(width=150, height=100)

# Entry
mile_input = Entry(width = 10)
mile_input.grid(row = 0, column = 1)
mile_input.get()

# Label
miles_label = Label(text ="Miles")
miles_label.grid(row = 0, column = 2)

is_equal_label = Label(text ="is equal to")
is_equal_label.grid(row = 1, column = 0)

kilometer_result_label = Label(text = "0")
kilometer_result_label.grid(row = 1, column = 1)

kilometer_label = Label(text ="Km")
kilometer_label.grid(row = 1, column = 2)

#Button
def calculate():

calculate_button = Button(text="Calculate", command=calculate)



window.mainloop()