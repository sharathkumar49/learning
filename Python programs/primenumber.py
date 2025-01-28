# A prime number has only two factors, which is 1 and the number itself.

n = int(input("Enter the number: "))

flag = False
if n > 1:
    for i in range(2,n):
        if n % i== 0:
            flag = True
            break
if(flag):
    print("it's not a prime number")
else:
    print("it's a prime number")


#Python Program to Print all Prime Numbers in an Interval
startvalue = int(input("Enter the start value: "))
endvalue = int(input("Enter the end value: "))
print("prime numbers between ", startvalue, " and ", endvalue, " are :")
for num in range(startvalue, endvalue+1):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num)