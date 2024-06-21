#rock paper scissors
import random
rock = '''
   _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
paper = '''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)

'''
scissors = '''

   _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

'''
game_images = [rock, paper, scissors]
userchoice = int(input("what do you choose? Type 0 for rock, 1 for paper, 2 for scissors\n"))
if userchoice >= 3 or userchoice < 0 :
    print("You typed an invalid number.")   
print(game_images[userchoice])

computer_choice = random.randint(0,2)
print("Computer chose:\n ")
print(game_images[computer_choice])

 
if userchoice == 0 and computer_choice == 2:
    print("You win!")
elif userchoice == 0 and computer_choice == 1:
    print("You Win!")
elif userchoice == 1 and computer_choice == 0:
    print("You Lose!")
elif userchoice == 1 and computer_choice == 2:
    print("You Win!")
elif userchoice == 2 and computer_choice == 1:
    print("You Lose!")
elif userchoice == 2 and computer_choice == 0:
    print("You Lose!")     
elif computer_choice > userchoice:
    print("You Lose")
elif computer_choice == userchoice:
    print("Its a draw!")    

                     
