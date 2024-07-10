def main():
    sum = int(input("enter a number: "))
    calculate_sum(sum)
def calculate_sum(n):
    for i in range(n):
       print("sum ", n*(n+1)/2)   
     
main()