height = float(input('enter your height cm: '))
weight = float(input('enter your weight in kg: ')) 
BMI = round(weight/(height*height))
if BMI<18.5  :
    print('under weight')
elif BMI > 18.5 and BMI <25:
    print('normal weight')
elif BMI > 25 and BMI < 30:
    print('over weight')
elif BMI > 30 and BMI < 35:
    print('obese')
elif BMI > 35:
    print('clinically obese') 
else:       
    print('wrong input')
