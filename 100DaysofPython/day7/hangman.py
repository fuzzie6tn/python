import random
import hangman_stages

print(hangman_stages.logo)

from hangman_words import word_list
chosen_word = random.choice(word_list)
lives = 6
# print(chosen_word)    

display = []

word_length = len(chosen_word)

for _ in range(word_length):
    display += "_"
# print (display)

end_of_game = False
while not end_of_game:
    guess = input("Guess the letter: ").lower()

    if guess in display:
        print(f"You have already guessed the letter {guess}")

    for position in range(word_length):
        letter = chosen_word[position]
        # print(f"Current position : {position}\nCurrent letter: {letter}\nGuessed letter: {guess}")
        if letter == guess: 
            display[position] = letter
    print(display)        

    if guess is not chosen_word:
        print(f"You guessed {guess}, thats not in the word. You losed 1 life")
        lives-=1
        if lives==0:
            end_of_game = True
            print("You lose!")
    if "_"  not in display:
        end_of_game = True
        print("You Win!")
    from hangman_stages import stages
    print(stages[lives])
