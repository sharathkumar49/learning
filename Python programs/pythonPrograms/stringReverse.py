

# 1. Using String Slicing: 

'''
Parameters:
s: The original string.
start (optional): Starting index (inclusive). Defaults to 0 if omitted.
end (optional): Stopping index (exclusive). Defaults to the end of the string if omitted.
step (optional): Interval between indices. A positive value slices from left to right,
while a negative value slices from right to left. If omitted, it defaults to 1 (no skipping of characters).
'''

s= "something"
print(s[::-1])




'''
Note: Python string library does not support the in-built “reverse()” as done by other python containers like list, hence 
knowing other methods to reverse string can prove to be useful. This article discusses several ways to achieve it.
'''
# 2. Using loop
def rev(str):
    s = ''
    for i in str:
      s = i + s   #have a note here
    return s

value = input("Enter the string: ")
finalvalue = rev(value)
print(finalvalue)
'''
Explanation : In above code, we call a function to reverse a string, which iterates to every element and 
intelligently join each character in the beginning so as to obtain the reversed string.
'''




# 3. Using recursion
# Python code to reverse a string
# using recursion
def reverse(s):
	if len(s) == 0:
		return s
	else:
		return reverse(s[1:]) + s[0]

s = "Geeksforgeeks"

print ("The original string is : ",end="")
print (s)

print ("The reversed string(using recursion) is : ",end="")
print (reverse(s))

'''
Explanation : In the above code, string is passed as an argument to a recursive function to reverse the string. In the 
function, the base condition is that if the length of the string is equal to 0, the string is returned. If not equal to 0, the 
reverse function is recursively called to slice the part of the string except the first character and concatenate the first character 
to the end of the sliced string.
'''



#4. Using stack
'''
Reversing a string using a stack is a fun exercise that demonstrates how stacks work.
Here's a simple Python code snippet to show you how it can be done:
'''
class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)

def reverse_string(input_string):
    stack = Stack()
    
    # Push all characters of string into stack
    for char in input_string:
        stack.push(char)

    # Pop all characters from stack and put them back into the string
    reversed_string = ''
    while not stack.is_empty():
        reversed_string += stack.pop()

    return reversed_string

# Test the function
input_string = "Hello, World!"
print("Original String:", input_string)
print("Reversed String:", reverse_string(input_string))

