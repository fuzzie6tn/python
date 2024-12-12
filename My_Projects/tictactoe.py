import tkinter as tk
import tkinter.messagebox

root = tk.Tk()
# tk.title('Tic Tac Toe Game')

# game board to hold data

game_board = ["-", "-", "-",
              "-", "-", "-",
              "-", "-", "-"]

# know if game over
game_still_on = True

winner = None

# current player
current_player = "X"


# Play game
def play_game():
    # display game board
    display_game_board()

    while game_still_on:
        # Handle a turn
        handle_turn(current_player)

        # Check if game over
        check_if_game_over()

        # Flip to the other player
        flip_player()

    # print the winner or tie
    if winner == "X" or winner == "O":
        print(" Congratulations" + winner + "you won!")
    elif winner == None:
        print("Game draw.")


def display_game_board():
    print("\n")
    print(game_board[0] + " | " + game_board[1] + " | " + game_board[2] + "     1 | 2 | 3")
    print("---------")
    print(game_board[3] + " | " + game_board[4] + " | " + game_board[5] + "     4 | 5 | 6")
    print("---------")
    print(game_board[6] + " | " + game_board[7] + " | " + game_board[8] + "     7 | 8 | 9")
    print("\n")


def handle_turn(player):
    # input spot from player
    print(player + "'s turn.")
    spot = input("Choose a spot from 1-9: ")

    valid = False
    while not valid:

        while spot not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            spot = input("Hey! Choose a spot from 1-9: ")

        spot = int(spot) - 1

        if game_board[spot] == "-":
            valid = True
        else:
            print("Opps! You have entered an incorrect spot. Try again.")

    game_board[spot] = player

    # display game board
    display_game_board()


# Check if game over
def check_if_game_over():
    check_for_winner()
    check_for_tie()


# Check winner
def check_for_winner():
    global winner

    row_winner = check_rows()
    column_winner = check_columns()
    diagonal_winner = check_diagonals()
    # Determine the winner
    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None


def check_rows():
    global game_still_on

    row_1 = game_board[0] == game_board[1] == game_board[2] != "-"
    row_2 = game_board[3] == game_board[4] == game_board[5] != "-"
    row_3 = game_board[6] == game_board[7] == game_board[8] != "-"

    if row_1 or row_2 or row_3:
        game_still_on = False
    # Return  winner
    if row_1:
        return game_board[0]
    elif row_2:
        return game_board[3]
    elif row_3:
        return game_board[6]
    else:
        return None


def check_columns():
    global game_still_on

    column_1 = game_board[0] == game_board[3] == game_board[6] != "-"
    column_2 = game_board[1] == game_board[4] == game_board[7] != "-"
    column_3 = game_board[2] == game_board[5] == game_board[8] != "-"

    if column_1 or column_2 or column_3:
        game_still_on = False
    # Return the winner
    if column_1:
        return game_board[0]
    elif column_2:
        return game_board[1]
    elif column_3:
        return game_board[2]
    else:
        return None


def check_diagonals():
    global game_still_on

    diagonal_1 = game_board[0] == game_board[4] == game_board[8] != "-"
    diagonal_2 = game_board[2] == game_board[4] == game_board[6] != "-"

    if diagonal_1 or diagonal_2:
        game_still_on = False
    # Return the winner
    if diagonal_1:
        return game_board[0]
    elif diagonal_2:
        return game_board[2]
    else:
        return None


# check tie
def check_for_tie():
    global game_still_on

    if "-" not in game_board:
        game_still_on = False
        return True
    else:
        return False


# Flip the current player
def flip_player():
    global current_player

    if current_player == "X":
        current_player = "O"
    elif current_player == "O":
        current_player = "X"


# play game
play_game()

root.mainloop()