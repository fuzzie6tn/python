def add(*args):
    sum_of_arg = 0
    for n in args:
        sum_of_arg += n
    print(f"The sum of args is {sum_of_arg}")
# add(3,2,1,1,2,1)

# key word arguments - kwarg - it is basically a dictionary

def calculate(**kwarg):
    print(kwarg)
    for key, value in kwarg.items():
        print(f"{key}: {value}")
calculate(add = 4, multiply = 3)