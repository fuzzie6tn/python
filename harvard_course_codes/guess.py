def get_guess():
    #consider integer guess
    guess = int(input('enter the guess: '))
    return guess
def getguess():
    #consider string guess in this case
    guess = input('enter the guess: ')
    return guess
def main():
    guess = get_guess()
    if guess == 50:
        print('correct!')
    else:
        print('incorrect!')
    guess2 = getguess()
    if guess2 == "ten":
        print('ok yes it is ten, you got it!')
    else:
        print('oops looks like you got the wrong guess')
            
main()            