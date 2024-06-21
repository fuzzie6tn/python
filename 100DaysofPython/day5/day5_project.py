# password generator

import random

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

print("Welcome to password generator!")
letter_ = int (input("How many letters do you want in your password? "))
number_ = int(input("How many numbers do you want in your password? "))
symbols_ = int(input("How many symbols? "))
#this is not random
# password = ""
# for char in range(1  , letter_ + 1):
#     password += random.choice(letters)
# for char in range(1, number_ + 1):
#     password+=random.choice(numbers)
# for char in range(1, symbols_ +1 ):
#     password+= random.choice(symbols)
# hard level
password_list = []
for char in range(1  , letter_ + 1):
    password_list.append(random.choice(letters))
for char in range(1, number_ + 1):
    password_list.append(random.choice(numbers))
for char in range(1, symbols_ +1 ):
    password_list.append(random.choice(symbols))
# print(password_list)        
random.shuffle(password_list)
# print(f"password is {password_list}")

password=""
for char in password_list:
    password+=char

print(f"your password is {password}")    