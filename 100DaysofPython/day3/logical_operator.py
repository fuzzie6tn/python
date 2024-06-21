print("welcome to roller coster ride")
height = int(input("Enter you height in cm"))
bill = 0
if height > 120:
    print('can ride')
    age = int(input('what is your age'))
    
    if age < 12:
        bill = 5
        print('child tickets $5')
    elif age <=18:
        bill = 7
        print('Youth tickets are $7')     
    elif age >= 45 and age <= 55:
        bill = 0
        print("Your ticket is free")       
    else:
        bill = 25
        print('adult ticket are $25')

    wants_phto = input("Do you want a photo? ")
    if  wants_phto == "y":
        #add $3 to thier bill
        bill +=3      
    print(f"your final bill: {bill}", ".... Good luck....")    
else:
    print('cannot ride')    