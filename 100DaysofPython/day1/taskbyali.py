def main():
    sum = int(input("enter a number: "))
    calculate_sum(sum)
def calculate_sum(n):
    for i in range(n):
        n+=1
    print("sum ", n)    
main()