print('''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************''')

print(" Welcome to Treasure Island\n Your mission is to find the treasure")
turn = input("Turn left or right? ")
if turn == "left":
    sea = input("You are going towards the sea. Swim or wait for a boat? ").lower()
    if sea == "wait":
            print("Boat has arrived. Take the boat!\n ")
            input("Type 'ok' to confirm\nThere is a door on the island. ").lower()
            choose_door = input("Choose (Red, yellow, blue) door to look for the treasure.\n")
            if choose_door == 'red':
                print("There is fire! Game Over..!!")
            elif choose_door == 'blue':
                print("There is a lake. You drowned!\nGame Over!")    
            else:
                print("Yellow Door. You made it. You got the treasure. Lit!") 

    else:
          print("You drowned. Game Over!")        
else:
    print("Watch Out! You fell in a hole.\nGame Over")