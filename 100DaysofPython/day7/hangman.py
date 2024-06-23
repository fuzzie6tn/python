import random

word_list = ['ardvark', 'baboon', 'camel']

chosen_word = random.choice(word_list)
print(chosen_word)
display = []
for _ in chosen_word:
    display += "_"
print (display)
guess = input("Guess the letter: ").lower()

for letter in chosen_word:
    if letter == guess:
        print("Right!")
    else:
        print("Wrong!")    