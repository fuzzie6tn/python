import random 

# NUMBER_TO_GUESS = random.choice(0,100)
NUMBER_TO_GUESS = 50

print("Welcome to the Number guessing game\nI'm thinking a number between 1 and 100\n")
level = input("Choose a difficulty: easy or hard?\n")
    
if level == "easy":
    print("You have 10 attempts remaining to guess the number.")
    attempts = 10
    while attempts < 10:
        guess = int(input("Guess the number: "))
        if guess == NUMBER_TO_GUESS:
            print("You got it.")
        elif guess > NUMBER_TO_GUESS:    
            print("Too high")
        else:
            print("Too low") 

    attempts -= 1
    print(f"{attempts} left")
    print("You have used all your attempts")

elif level == "hard":
    print("You have 5 attempts remaining to guess the number.")
    attempts = 5
    while not attempts:
        guess = input("Guess the number: ")
        if guess == NUMBER_TO_GUESS:
            print("You got it.")
        elif guess > NUMBER_TO_GUESS:    
            print("Too high")
        else:
            print("Too low") 

        attempts -= 1
        print(f"{attempts} left")
    print("You have used all your attempts")
        
else:
    print(f"{level} is not in this game")    