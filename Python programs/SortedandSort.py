

#source: https://www.geeksforgeeks.org/python-difference-between-sorted-and-sort/

'''
Sorting means rearranging a given sequence of elements according to a comparison operator on the elements. The comparison operator 
is used to decide the new order of the element in the respective data structure.

In Python, sorting any sequence is very easy as it provides in-built methods for sorting. Two such methods are sorted() and sort(). 
These two methods are used for sorting but are quite different in their own way. Lets have a look at them one by one.

sorted():
sorted() method sorts the given sequence as well as set and dictionary(which is not a sequence) either in ascending order or in 
descending order(does unicode comparison for string char by char) and always return the a sorted list. This method doesnot effect 
the original sequence.
 

Syntax: sorted(iterable, key, reverse=False)
Parameters: 
Iterable: sequence (list, tuple, string) or collection (dictionary, set, frozenset) or any other iterator that needs to be sorted. 
Key(optional): A function that would serve as a key or a basis of sort comparison. 
Reverse(optional): If set True, then the iterable would be sorted in reverse (descending) order, by default it is set as False.
Return Type: Returns a sorted list. 

'''
# Python program to demonstrate
# sorted()
L = [1, 2, 3, 4, 5]

print("Sorted list:")
print(sorted(L))

print("\nReverse sorted list:")
print(sorted(L, reverse = True))

print("\nOriginal list after sorting:")
print(L)



#Example 2: Sorting different data types
# Python program to demonstrate
# sorted()


# List
x = ['q', 'w', 'r', 'e', 't', 'y']
print(sorted(x))

# Tuple
x = ('q', 'w', 'e', 'r', 't', 'y')
print(sorted(x))

# String-sorted based on ASCII translations
x = "python"
print(sorted(x))

# Dictionary
x = {'q':1, 'w':2, 'e':3, 'r':4, 't':5, 'y':6}
print(sorted(x))

# Set
x = {'q', 'w', 'e', 'r', 't', 'y'}
print(sorted(x))


'''
Using key parameter:
This optional parameter key takes a function as it's value. This key function transforms each element before sorting, it takes the 
value and returns 1 value which is then used within sort instead of the original value.
Example: Let's suppose we want to sort a List of string according to its length. This can be done by passing the len() function as 
the value to the key parameter. Below is the implementation.
'''
# Python program to demonstrate
# sorted()
L = ['aaaa', 'bbb', 'cc', 'd']

# sorted without key parameter
print(sorted(L))
print()

# sorted with key parameter
print(sorted(L, key = len))


'''
sort()
sort() function is very similar to sorted() but unlike sorted it returns nothing and makes changes to the original sequence. 
Moreover, sort() is a method of list class and can only be used with lists.
 

Syntax: List_name.sort(key, reverse=False)
Parameters: 
key: A function that serves as a key for the sort comparison. 
reverse: If true, the list is sorted in descending order.
Return type: None 
'''
# Python program to demonstrate
# sort()

# List of Integers
numbers = [1, 3, 4, 2]

# Sorting list of Integers
numbers.sort()

print(numbers)

# List of Floating point numbers
decimalnumber = [2.01, 2.00, 3.67, 3.28, 1.68]

# Sorting list of Floating point numbers
decimalnumber.sort()

print(decimalnumber)

# List of strings
words = ["Geeks", "For", "Geeks"]

# Sorting list of strings
words.sort()

print(words)



#Example 2: Sorting in reverse order.
# Python program to demonstrate
# sort()


# List of Integers
numbers = [1, 3, 4, 2]

# Sorting list of Integers
numbers.sort(reverse = True)

print(numbers)

# List of Floating point numbers
decimalnumber = [2.01, 2.00, 3.67, 3.28, 1.68]

# Sorting list of Floating point numbers
decimalnumber.sort(reverse = True)

print(decimalnumber)

# List of strings
words = ["Geeks", "For", "Geeks"]

# Sorting list of strings
words.sort(reverse = True)

print(words)



#Example 3: Using key parameter.
# Python program to demonstrate sorting by user's
# choice

# function to return the second element of the
# two elements passed as the parameter
def sortSecond(val):
	return val[1]

# list1 to demonstrate the use of sorting
# using using second key
list1 = [(1, 2), (3, 3), (1, 1)]

# sorts the array in ascending according to
# second element
list1.sort(key = sortSecond)
print(list1)

# sorts the array in descending according to
# second element
list1.sort(key = sortSecond, reverse = True)
print(list1)

