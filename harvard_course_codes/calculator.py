# x = float(input("what is x? "));
# y = float(input("what is y? "));
# # print(int(x)+int(y));  #dont use only x and y it will concatinate it  
# z =  x/y
# # print(f'{z:.2f}') #this is going to round off by 2 digit 
# print(f'{z}')
def main():
    x = int(input('value of x? '))
    print(x, ' square is ', square(x))
def square(n):
    return n**2
main()    

