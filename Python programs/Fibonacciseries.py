# Fibonacci series has numbers in which each number is the sum of two preceding numbers
# 0 1 1 2 3 5 8 ....

noofterms = int(input("enter the no of values: "))
a , b, count  = 0, 1, 0

if noofterms <= 0 :
    print("please enter a positive integer")
elif noofterms == 1:
    print("fibonacci series upto 1", b)
else:
    print("Fibonacci series : ", end ="")
    print(a, b, end=" ")
    while count < noofterms :
        c = a + b
        b = c
        a = b
        count += 1
        print(c, end=" ")
