def main():
    x = int(input("enter a number: "))
    if is_even(x):
        print("even")
    else:
        print("odd")
def is_even(n):
    # if n%2 == 0:
    #     return True
    # else:
    #     return False
    return True if n%2==0 else False
main()             
