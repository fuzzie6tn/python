def pin():
    p = int(input('Enter your ATM 4 digit pin: '))
    print('Welcome!')
    transaction()
def transaction():
    choose = int(input('Choose the type of transaction\n 1. withdraw 2. deposit 3. default\n'))
    match choose:
        case 1:
            withdrawal()
        case 2:
            deposit()
        case 3:
            default()
        case _:
            print('invalid choice!')
def withdrawal():
    amount = int(input('enter the amount you want to withdraw? '))
    return amount
    print(amount, ' has been deducted from your account')
def deposit():
    acc_number = int(input('Enter the account number: '))
    send = int(input('enter the amount you want to deposit to ', acc_number))    
    print('Sent successfully!')
def default():
    amount = int(input('enter the amount you want to withdraw? '))
    return amount
    print(amount, ' has been deducted from your account')

pin()       
