# i=-1
# while i!=0:
#     print('meow')
#     i=i-1

# print("meow\n"*3, end="")

# while True:
#     n = int(input("what is n? "))
#     if n>0:
#         break

# for _ in range(n):
#         print('meow')

def main():
    number = get_number()
    meow(number)

def get_number():
    while True:
        n = int(input("what the number? "))
        if n>0:
            break
    return n 
def meow(n):
    for _ in range(n):
        print('meow')    

main()














