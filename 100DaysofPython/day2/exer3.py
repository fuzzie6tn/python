# using mathematical operation - fstring 
# how many days weeks and months left in ur life if we were lucky enough to live life for 90 years
# 1 year = 365 days
# 1 year - 52 weeks
# 1 year - 12 months

# 90 years = 4770 weeks
# 90 years = 32, 850 days
# 90 years = 1080 months
age = int(input("your age?"))
years_remaining = 90 - age
days_remaining = years_remaining * 365
weeks_remaining = years_remaining * 52
months_remaining = years_remaining *12
print(f"You have {weeks_remaining} weeks, {months_remaining} months and {days_remaining} days left")