def prime_num_checker(num):
    is_prime = True
    for i in range (2,num-1):
        if num % i == 0:
            is_prime = False
    if is_prime:
        print("its a prime number")
    else:
        print(" its not a prime number")
num = int(input("enter any number "))
prime_num_checker(num)