#display art
from art import logo, vs
from gamedata import data
import random
import os
score = 0
game_should_continue =True
accountB = random.choice(data)


def clear():
    """Clear the console for a new game"""
    os.system('cls' if os.name == 'nt' else 'clear')
def format_data(account):
        '''Format the account data into printable format'''
        account_name = account["name"]
        account_desc = account["description"]
        account_country = account["country"]
        return(f"{account_name}, a {account_desc} from {account_country}")
def check_answer(guess, a_followers, b_followers):
    '''     take the user guess and follower counts and returns if they got it right   '''

    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"
print(logo)
while game_should_continue:
    # Generate a random account from the game data
    accountA = accountB
    accountB = random.choice(data)
    while accountA == accountB:  
        accountB = random.choice(data) #regenerated B if they both are same. 

    print(f"Compare A: {format_data(accountA)}.")
    print(vs)
    print(f"Against B: {format_data(accountB)}.")

    # Ask user for a guess for who has more follwers
    guess = input("Who has more followers has  more followers A or B? ").lower()


    #Check if the user is correct
    #Get the follower count of each account
    a_follower_count = accountA["follower_count"]
    b_follower_count = accountB["follower_count"]
    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    clear()
    print(logo)
    #give user feedback 

    if is_correct:
        score += 1
        print(f"You are right! Current score {score}")
    else :
        game_should_continue = False
        print(f"sorry, thats wrong. Final Score {score}") 
