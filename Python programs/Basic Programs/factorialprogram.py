# factorial = factorial of a number is denoted by n! , 5! = 5 * 4 * 3 * 2 * 1

#Example 1

def fact(num):
    if num == 1:
        return num
    else:
        return num * fact(num - 1)

result = fact(4)
print(result)