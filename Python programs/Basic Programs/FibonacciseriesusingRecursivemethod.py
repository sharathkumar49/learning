
#Python program to print Fibonacci series using recursive methods
n = int(input("Enter the number of values: "))
def fibo(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fibo(num-1) +fibo(num - 2)

for i in range(0,n):
    print(fibo(i))
  
