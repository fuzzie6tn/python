from tkinter import *
from tkinter import messagebox
import random
import json
# import pyperclip


# ------------ Password generate -------------------- #

def generate_password():

    letters = [
        "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", 'K', "L", 'M', 'N', "O", 'P', 'Q', "R", 'S', 'T', 'U', "V", "W", 'X'," Y",' Z'
        , "a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","a","v","w","x","y","z"

    ]
    numbers = [
        "0","1","2","3","4","5","6","7","8","9",
    ]
    symbols = [
        "!","-","+","@","$","#",")","(","%","|",
    ]
    nr_letters = random.randint(8,10)
    nr_symbols = random.randint(2,4)
    nr_numbers = random.randint(2,4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    # for char in range(nr_letters):
    #     password_list.append(random.choice(letters))
    password_symbol = [ random.choice(symbols) for _ in range(nr_symbols)]
    # for char in range(nr_symbols):
    #     password_list.append(random.choice(symbols))
    password_number = [random.choice(symbols) for _ in range(nr_numbers)]
    # for char in range(nr_numbers):
    #     password_list.append(numbers)

    password_list = password_letters + password_symbol + password_number

    random.shuffle(password_list)
    password = "".join(password_list)
    # password = ""
    # for char in password_list:
    #     password+=char
    pass_entry.insert(0, password)
    # pyperclip.copy(password)
    # print(f'Your password is: {password}')

# ----------- Save Password ------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = pass_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(password)==0 or len(email)==0:
        messagebox.showinfo(title='Oops', message='Please don\'t leave any entry empty!')
    else:
        try:
            # write data in json file - .dump()  - to read data from json file (.load()) - to update data from json file (.update)
            with open("data.json", "r") as data_file:
              # reading the old data
               data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
           # updating the old data
            data.update(new_data)

            with open("data.json", "w") as data_file:
               # saving the old data
                json.dump(data, data_file,indent=4)

        finally:
            pass_entry.delete(0, END)
            website_entry.delete(0, END)


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
generate_button = Button(text="Generate Password", bg="white",width=15, command=generate_password)
generate_button.grid(column=2, row=3,padx=(0, 10))

add_button = Button(text="Add", width=41, bg="white",command=save)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()