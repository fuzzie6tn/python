import random

def deal_card():
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    sum(cards) # sum of cards
    if sum(cards) == 21 and len(cards) == 2: #checkin if blackjack
        return 0
    
    if 11 in cards and sum(cards)>21:   #checking if ace 11 and appending it with 1
        cards.remove(11)
        cards.append(1)

    return sum(cards)

user_card = []
computer_card = []
is_game_over = False

for _ in range(2):
    user_card.append(deal_card())
    computer_card.append(deal_card())
while not is_game_over:
    user_score = calculate_score(user_card)
    computer_score = calculate_score(computer_card)   
    print(f"Your cards: {user_card}, current score: {user_score}")
    print(f"Computer's first card: {computer_card[0]}")

    if user_score == 0 or computer_score == 0 or user_score > 21:
        is_game_over = True
    else:
        user_should_deal = input("type 'y' to get another card , type 'n' to pass:\n")  
        if user_should_deal == "y":
            user_card.append(deal_card())  
        else:
            is_game_over = True    
while computer_score !=0 and computer_score < 17:
    computer_card.append(deal_card())
    computer_score = calculate_score(computer_card)            