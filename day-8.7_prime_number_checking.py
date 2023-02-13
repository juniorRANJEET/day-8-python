print("prime number checking ")
num = int(input("enter any number "))
for i in range (2,num-1):
    if num % i == 0:
        print(" not prime number")
    else:
        print("prime")
