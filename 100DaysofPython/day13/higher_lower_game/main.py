# import random
# from art import logo, vs
# from gamedata import data

# print(logo)

# # Ensure data has at least two items
# if len(data) < 2:
#     raise ValueError("Not enough data to compare")

# # Randomly select two different items
# item_a, item_b = random.sample(data, 2)

# # Print comparison for item A
# print(f"Compare A: {item_a['name']} a {item_a['description']} from {item_a['country']}")

# print(vs)

# # Print comparison for item B
# print(f"Compare B: {item_b['name']} a {item_b['description']} from {item_b['country']}")

# # Ask the user for input
# answer = input("Who has more followers? Type 'A' or 'B': ")
# ----------------------------------------------------------------------------------------------------

#display art
from art import logo
from gamedata import data
import random

print(logo)
# we made this function more reusable for both accounts
def format_data(account):
    '''Format the account data into printable format'''
    account_name = account["name"]
    account_desc = account["description"]
    account_country = account["country"]
    print(f"{account_name}, a {account_desc} from {account_country}")


# Generate a random account from the game data
accountA = random.choice(data)
accountB = random.choice(data)
if accountA == accountB:
    accountB = random.choice(data) #regenerated B if they both are same. 





# Ask user for a guess

#Check if the user is correct


