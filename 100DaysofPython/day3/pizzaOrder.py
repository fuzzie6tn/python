print("***Welcome to python pizza delieveries!***")

print(" Small pizza $15\n Medium pizza $20\n Large pizza $25")
size = input("what size of pizza do you want? (S,M or L) ")

print(" Pepperoni for small pizza: $2\n Pepperoni for large pizza: $3")
pepperoni = input("Do you want pepperoni on it? (y or n) ")

print("Extra cheese for any pizza: $1")
extra_cheese = input("Do you want extra cheeze? (y or n) ")
bill = 0
if size == "s":
    bill += 15
    if pepperoni == "y":
        bill +=2
        if extra_cheese == "y":
            bill += 1  
    print(f"Final bill is: {bill}")          
elif size == "m":
    bill += 20
    if pepperoni == "y":
        bill += 3
        if extra_cheese == "y":
            bill += 1   
    print(f"Final bill is: {bill}")              
elif size == "l":
    bill += 25
    if pepperoni == "y":
        bill += 3
        if extra_cheese == "y":
            bill += 1        
    print(f"Final bill is: {bill}")          
else:
    print("you entered wrong size")                    
