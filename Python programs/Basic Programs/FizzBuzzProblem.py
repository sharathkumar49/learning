

def fizz_buzz(number):
    if(number % 3 == 0) and (number % 5 == 0):
        return "fizzbuzz"
    if number % 3 == 0:
        return "fizz"
    if number % 5 == 0:
        return "buzz"
    return number


num = int(input("Enter the number: "))
print(fizz_buzz(num))