import random

def deal_card():
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    card = random.choice(cards)
    return card

user_card = []
computer_card = []

for _ in range(2):
    user_card.extend(deal_card())
    computer_card.extend(deal_card())
print(user_card)
print(computer_card)    