import random 
#I HAVE DONE THIS BY MYSELF!!!!
# NUMBER_TO_GUESS = random.choice(1,100)
# NUMBER_TO_GUESS = 50

from logo import logo
print(logo)
print("Welcome to the Number guessing game\nI'm thinking of a number between 1 and 100\n")

NUMBER_TO_GUESS = random.choice(range(1, 101))

# for num in range(1, 101):
#     print(num)

def gues_the_num():
    level = input("Choose a difficulty: easy or hard?\n")

    if level == "easy":
        print("You have 10 attempts remaining to guess the number.")
        attempts = 10
        while attempts:
            guess = int(input("Guess the number: "))
            if guess == NUMBER_TO_GUESS:
                print("You got it.")
                break
            elif guess > NUMBER_TO_GUESS:    
                print("Too high")
            else:
                print("Too low") 

            attempts -= 1
            print(f"You have {attempts} attempts left")
        print("You have used all your attempts")

    elif level == "hard":
        print("You have 10 attempts remaining to guess the number.")
        attempts = 5
        while attempts:
            guess = int(input("Guess the number: "))
            if guess == NUMBER_TO_GUESS:
                print("You got it.")
                break
            elif guess > NUMBER_TO_GUESS:    
                print("Too high")
            else:
                print("Too low") 

            attempts -= 1
            print(f"You have {attempts} attempts left")
        print("BYE")
            
    else:
        print(f"{level} is not in this game")    

gues_the_num()        