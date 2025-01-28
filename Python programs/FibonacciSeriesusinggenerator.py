
n = int(input("Enter the number of values: "))
def fibo(num):
    if num == 0:
        return 0
    if num == 1:
        return 1
    return fibo(num-1) +fibo(num - 2)

for i in range(0,n):
    print(fibo(i))

