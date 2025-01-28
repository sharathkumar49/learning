

'''
Python string library does’nt support the in-built “reverse()” as done by other python containers like list, hence 
knowing other methods to reverse string can prove to be useful. This article discusses several ways to achieve it.
'''
#Using loop
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




#Using recursion
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



#Using stack


