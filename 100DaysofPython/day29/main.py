from tkinter import *
from tkinter import messagebox

from docutils.nodes import title
from docutils.parsers.rst.directives.misc import Title


# ------------ Password generate -------------------- #

# ----------- Save Password ------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = pass_entry.get()

    is_ok = messagebox.askokcancel(title=website, message=f'These are the details entered:\nEmail: {email}\nPassword: {password}\nIs it ok to save?')
    if is_ok:
        with open("data.txt", "a") as data_file:
            data_file.write(f"{website} | {email} | {password}\n")
            website_entry.delete(0, END)
            pass_entry.delete(0, END)
            email_entry.delete(0, END)

# Create window
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg="white")

# Canvas for logo
canvas = Canvas(width=200, height=200, bg="white", highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# Labels
website_label = Label(text="Website:", bg="white")
website_label.grid(column=0, row=1)
email_label = Label(text="Email/Username:", bg="white")
email_label.grid(column=0, row=2)
pass_label = Label(text="Password:", bg="white")
pass_label.grid(column=0, row=3)

# Entries
website_entry = Entry(width=40)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()
email_entry = Entry(width=40)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "fazi@gmail.com")
pass_entry = Entry(width=28)
pass_entry.grid(column=1, row=3)

# Buttons
generate_button = Button(text="Generate Password", bg="white",width=15)
generate_button.grid(column=2, row=3,padx=(0, 10))

add_button = Button(text="Add", width=41, bg="white",command=save)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()