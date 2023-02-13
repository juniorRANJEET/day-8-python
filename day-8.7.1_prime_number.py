def prime_num_checker(num):
    n = True
    for i in range (2,num-1):
        if num % i == 0:
            n = False
    if n == True:
        print("its a prime number")
    else:
        print(" its not a prime number")
num = int(input("enter any number "))
prime_num_checker(num)