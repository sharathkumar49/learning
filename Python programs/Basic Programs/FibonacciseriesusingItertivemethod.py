first, second = 0, 1
n = int(input("Enter the number of values: "))
if n <= 1:
    print(second)
else:
    print(first,second, end=" ")
    for i in range(2, n+1):
        result = first + second
        print(result, end= " ")
        second = result
        first = second
        