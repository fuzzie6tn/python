from tkinter import *

# ------------ Password generate -------------------- #

# ----------- Save Password ------------------------- #

# --------- UI setup -------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20, bg="White")

# Image
canvas = Canvas(width=200, height=200, bg="White", highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100,100, image=logo_img)
canvas.grid(column=1, row=0)

# Website label
website_label = Label(text="Website", bg="White")
website_label.grid(column=0, row=1)

# Website entry
website_entry = Entry(width=35)
website_entry.grid(columnspan=2, column=1,row=1)

# Email-username label
email_label = Label(text="Email/Username", bg="White")
email_label.grid(column=0, row=2)

# Email entry
email_entry = Entry(width=35)
email_entry.grid(columnspan=2, column=1,row=2)

# Password label
pass_label = Label(text="Password", bg="White")
pass_label.grid(column=0, row=3)

# Password entry
pass_entry = Entry(width=21)
pass_entry.grid(column=1,row=3)

# Generate Password Button
generate_button = Button(text="Generate Password", bg="White")
generate_button.grid(column=2, row=3)

# Add Button
add_button = Button(text="Add", bg="White", width=36)
add_button.grid(columnspan = 2,column=1, row=4)


window.mainloop()