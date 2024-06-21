#calculating BMI
# weight(kg)/height ^2(m^2)

weight = float(input("what i your weight in kg\n"))
height = float(input("what is you height in meters\n"))

BMI = int(weight/(height*height)) #or height**2 
print("BMI is", BMI)