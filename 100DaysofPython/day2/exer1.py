# given 2 digit random number 
#  add the first digit to second digit 
# numerical result
# 39

digit = input("Enter two digit number")
print(type(digit))

first = digit[0] #subscripting
second = digit[1]
result = int(first) + int (second)
print(result)


