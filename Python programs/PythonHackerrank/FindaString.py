
# In this challenge, the user enters a string and a substring. You have to print the number of times that the substring occurs in the given string. String traversal will take place from left to right, not from right to left.

# NOTE: String letters are case-sensitive.

# Input Format:
# The first line of input contains the original string. The next line contains the substring.

# Constraints:
# Each character in the string is an ascii character.

# Output Format:
# Output the integer number indicating the total number of occurrences of the substring in the original string.

# Sample Input:
# ABCDCDC
# CDC


# Sample Output:
# 2


# Concept:

# There are a couple of new concepts:
# In Python, the length of a string is found by the function len(s), where  is the string.

# To traverse through the length of a string, use a for loop:
# for i in range(0, len(s)):
#     print (s[i])

# A range function is used to loop over some length:
# range (0, 5)
# Here, the range loops over 0 to 4. 5 is excluded.



# Constraints

# -


def count_substring(string, sub_string):
    count = 0
    for i in range(len(string) - sub_string + 1):
        if string[i:i+len(sub_string)] == sub_string:
            count += 1
        
    return count

if __name__ == '__main__':
    string = input().strip()



# Solution 2

# Using str.find() in a Loop
# You can repeatedly use str.find() to locate the substring and count occurrences:

# def count_substring(string, sub_string):
#     count = 0
#     start = 0
#     while start < len(string):
#         pos = string.find(sub_string, start)
#         if pos != -1:
#             count += 1
#             start = pos + 1
#         else:
#             break
#     return count

# if __name__ == '__main__':
#     string = input().strip()
#     sub_string = input().strip()
    
#     count = count_substring(string, sub_string)
#     print(count)