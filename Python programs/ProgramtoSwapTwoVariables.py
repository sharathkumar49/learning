# Python program to swap two variables

x = 5
y = 10

# To take inputs from the user
#x = input('Enter value of x: ')
#y = input('Enter value of y: ')

# create a temporary variable and swap the values
temp = x
x = y
y = temp

print('The value of x after swapping: {}'.format(x))
print('The value of y after swapping: {}'.format(y))



#Source Code: Without Using Temporary Variable
x = 5
y = 10

x, y = y, x
print("x =", x)
print("y =", y)



#Using addition and subtraction
print("initial value  of x and y before swapping", x, y)
x, y  = 5, 10
x = x + y
y = x - y
x = x - y
print("After swapping using addition and subtraction")
print("x =", int(x))
print("y =", int(y))


#Multiplication and Division
print("initial value  of x and y before swapping", x, y)
x, y  = 5, 10
x = x * y
y = x / y
x = x / y
print("After swapping using multiplication and division")
print("x =", int(x))
print("y =", int(y))


#XOR swap
#This algorithm works for integers only
print("Using xor operation")
x, y  = 5, 10
x = x ^ y
y = x ^ y
x = x ^ y
print("The value of x and y after swapping")
print("x =", int(x))
print("y =", int(y))
