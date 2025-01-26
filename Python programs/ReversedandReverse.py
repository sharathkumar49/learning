
#Source:  https://www.geeksforgeeks.org/python-reversed-function/


'''
Python reversed() function:
Python reversed() method returns an iterator that accesses the given sequence in the reverse order.

Python reversed() Syntax:
reversed(sequ) 
sequ : Sequence to be reversed. 

Python reversed() Returns:
returns an iterator that accesses the given sequence in the reverse order. 

'''

#How to use the reversed method in Python?

#Example 1: Demonstration of Python reversed() method
#Here we use tuple and range.

# Python code to demonstrate working of
# reversed()

# For tuple
seqTuple = ('g', 'e', 'e', 'k', 's')
print(list(reversed(seqTuple)))

# For range
seqRange = range(1, 5)
print(list(reversed(seqRange)))



#Example 2: reversed() in custom objects
class gfg:
	vowels = ['a', 'e', 'i', 'o', 'u']

	# Function to reverse the list
	def __reversed__(self):
		return reversed(self.vowels)

# Main Function
if __name__ == '__main__':
	obj = gfg()
	print(list(reversed(obj)))



#Example 3: Python List reverse()
vowels = ['a', 'e', 'i', 'o', 'u']
print(list(reversed(vowels)))


#Example 4: Python reverse() string
str = "Geeksforgeeks"
print(list(reversed(str)))


#Example 5: Python reverse() list
# For list
seqList = [1, 2, 4, 3, 5]
print(list(reversed(seqList)))



'''
Python List reverse():
Python List reverse() is an inbuilt method in the Python programming language that reverses objects of the List in place.

Syntax: 
list_name.reverse()

Parameters: 
There are no parameters.

Returns: 
The reverse() method does not return any value but reverses the given object from the list.

Error:
When anything other than list is used in place of list, then it returns an AttributeError
'''
#Example 1: Reverse a List
# Python3 program to demonstrate the
# use of reverse method

# a list of numbers
list1 = [1, 2, 3, 4, 1, 2, 6]
list1.reverse()
print(list1)

# a list of characters
list2 = ['a', 'b', 'c', 'd', 'a', 'a']
list2.reverse()
print(list2)


#Note: reverse() is used with list only, not any iterables or collections.
#Only the list uses reverse() method

'''
Example 3: Practical Application
Given a list of numbers, check if the list is a palindrome. 

Note: Palindrome-sequence that reads the same backward as forwards.
'''
# Python3 program for the
# practical application of reverse()

list1 = [1, 2, 3, 2, 1]

# store a copy of list
list2 = list1.copy()

# reverse the list
list2.reverse()

# compare reversed and original list
if list1 == list2:
	print("Palindrome")
else:
	print("Not Palindrome")


#String Palindrome using this list reverse method
batman = 'malayalam'
list1 = list(batman)
list2 = list1.copy()
list2.reverse()
if list2 == list1:
    print("it is palindrome")
else:
    print("it is not a palindrome")

