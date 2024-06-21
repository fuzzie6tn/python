#tip % = tip/100
#total tip = bill*tip%
# total_bill = bill + total tip
# bill per person = total bill /people
# final amount = round(bill person,2)
print("welcome to the tip calculator")

total_bill = float(input("What is the total amount of bill? $"))

tip = int(input("what percentage tip would you like to give? 10, 12, or 15?"))

split = int(input("how many people to split the bill?"))

calculate_tip = float(round((tip / 100) * total_bill + total_bill, 2))

print(f"Each person should pay: ${calculate_tip}")

