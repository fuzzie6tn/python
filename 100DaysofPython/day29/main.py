from tkinter import *

# ------------ Password generate -------------------- #

# ----------- Save Password ------------------------- #

# --------- UI setup -------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20, bg="White")
window.geometry("500x500")
# Image

canvas = Canvas(width=200, height=200, bg="White", highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100,100, image=logo_img)

canvas.pack()
window.mainloop()