# try:
#     x = int (input('what is x?'))
#     print(f'x is {x}')

# except ValueError:
#     print('x is not an integer')    
try:
    x = int(input('what is x?'))
except:
    print('x is not an interger')
else:
    print(f'x is {x}')    