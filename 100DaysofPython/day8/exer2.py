def prime_n(number):
    isPrime = True
    for i in range(2, number):
        if number % i == 0:
            isPrime = False
    if isPrime:
        print("It is a prime number")
    else:
        print("It is not a prime number")            

n = int(input("check the number: "))
prime_n(number=n)
