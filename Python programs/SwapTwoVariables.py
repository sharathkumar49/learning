
# Python program to swap two variables in a single line
x = 5
y = 10
x, y = y, x
print("After Swapping values of x and y are", x, y)




#Method 1 (Using Arithmetic Operators) 
a = int(input("Enter the first value:"))
b = int(input("Enter the second value:"))
print("So a =", a, "and b =", b)
a = a + b
b = a - b
a = a - b
print("After swapping a =", a, "b = ", b)

'''
(or)
a=a-b
b=a+b
a=b-a
'''

#Multiplication and division can also be used for swapping.  
x = 10
y = 5
x = x * y  # x now becomes 50
y = x // y;  # y becomes 10
x = x // y;  # x becomes 5

print("After Swapping: x =", x, " y =", y);




'''
Method 2 (Using Bitwise XOR) :
The bitwise XOR operator can be used to swap two variables. The XOR of two numbers x and y returns a number that has 
all the bits as 1 wherever bits of x and y differ. For example, XOR of 10 (In Binary 1010) and 5 (In Binary 0101) is 1111 and 
XOR of 7 (0111) and 5 (0101) is (0010). 
'''
# Python3 code to swap using XOR
x = 10
y = 5

# Code to swap 'x' and 'y'
x = x ^ y; # x now becomes 15 (1111)
y = x ^ y; # y becomes 10 (1010)
x = x ^ y; # x becomes 5 (0101)

print ("After Swapping: x = ", x, " y =", y)

'''
Problems with the above methods 
1) The multiplication and division based approach doesnt work if one of the numbers is 0 as the product becomes 0 irrespective of the other number.
2) Both Arithmetic solutions may cause an arithmetic overflow. If x and y are too large, addition and multiplication may go out of integer range.
3) When we use pointers to variable and make a function swap, all the above methods fail when both pointers point to the same variable. Let’s take a look at what will happen in this case if both are pointing to the same variable.

// Bitwise XOR based method 
x = x ^ x; // x becomes 0 
x = x ^ x; // x remains 0 
x = x ^ x; // x remains 0
// Arithmetic based method 
x = x + x; // x becomes 2x 
x = x - x; // x becomes 0 
x = x - x; // x remains 0

Let us see the following program. 
'''
def swap(xp, yp):

	xp[0] = xp[0] ^ yp[0]
	yp[0] = xp[0] ^ yp[0]
	xp[0] = xp[0] ^ yp[0]


# Driver code
x = [10]
swap(x, x)
print("After swap(&x, &x): x = ", x[0])

'''
Swapping a variable with itself may be needed in many standard algorithms. For example, see this implementation of QuickSort 
where we may swap a variable with itself. The above problem can be avoided by putting a condition before the swapping.
'''
# Python3 program of above approach
def swap(xp, yp):

	# Check if the two addresses are same
	if (xp[0] == yp[0]):
		return
	xp[0] = xp[0] + yp[0]
	yp[0] = xp[0] - yp[0]
	xp[0] = xp[0] - yp[0]


# Driver Code
x = [10]
swap(x, x)
print("After swap(&x, &x): x = ", x[0])

# This code is contributed by SHUBHAMSINGH10





'''
Method 3 (A mixture of bitwise operators and arithmetic operators) 
The idea is the same as discussed in Method 1 but using Bitwise addition and subtraction for swapping. 

Below is the implementation of the above approach. 
'''
# Python3 program to swap two numbers
# Function to swap the numbers
def swap(a, b):
	a = (a & b) + (a | b)  # Same as a = a + b
	b = a + (~b) + 1  # Same as b = a - b
	a = a + (~b) + 1  # Same as a = a - b
	print("After Swapping: a = ", a, ", b = ", b)

# Driver code
a = 5
b = 10
# Function call
swap(a, b)



