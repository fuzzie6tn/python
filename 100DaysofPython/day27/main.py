import tkinter

window = tkinter.Tk()
window.title("Gui")
window.minsize(width=500, height=300)

# label
my_label = tkinter.Label(window, text="Hello World", font=("Arial", 24, "bold"))
my_label.pack() # this will automatically bring it to the center

window.mainloop()