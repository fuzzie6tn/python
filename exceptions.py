# try:
#     x = int (input('what is x?'))
#     print(f'x is {x}')

# except ValueError:
#     print('x is not an integer')  
# ----------  
# try:
#     x = int (input('what is x?'))
# except ValueError:
#     print('x is not an integer')    
# print(f'x is {x}')
# to solve this 
# -------
# try:
#     x = int(input('what is x?'))
# except:
#     print('x is not an interger')
# else:
#     print(f'x is {x}')    
# prompting user to enter value again and again
# --------------

# while True:
#     try:
#         x = int(input('what is x?'))

#     except ValueError:
#         print('x is not and integer')
#     else:
#         break    
# print(f'x is {x}')        
# def main():
#     x = getint()
#     print(f'x is {x}')
# def getint():
#     while True:
#         try:
#             return int(input('what is x?'))
#         except ValueError:
#             print('x is not an integer')
# main()

def main():
    x = get_int('whats x?' )
    print(f'x is {x}')
def get_int(prompt): #prompting user
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            pass    
main()        