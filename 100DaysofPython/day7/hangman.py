import random
import hangman_stages
import hangman_words

print(hangman_stages)
chosen_word = random.choice(hangman_words)
lives = 6
print(chosen_word)

display = []

word_length = len(chosen_word)

for _ in chosen_word:
    display += "_"
print (display)

end_of_game = False
while not end_of_game:
    guess = input("Guess the letter: ").lower()

    for position in range(word_length):
        letter = chosen_word[position]
        # print(f"Current position : {position}\nCurrent letter: {letter}\nGuessed letter: {guess}")
        if letter == guess: 
            display[position] = letter
    print(display)        

    if guess is not chosen_word:
        lives-=1
        if lives==0:
            end_of_game = True
            print("You lose!")
    if "_"  not in display:
        end_of_game = True
        print("You Win!")

    print(hangman_stages[lives])
