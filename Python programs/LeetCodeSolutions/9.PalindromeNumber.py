# 9. Palindrome Number
# Given an integer x, return true if x is a palindrome, and false otherwise.
#
# Example 1:
# Input: x = 121
# Output: true
#
# Example 2:
# Input: x = -121
# Output: false
#
# Example 3:
# Input: x = 10
# Output: false
#
# Constraints:
# -2^31 <= x <= 2^31 - 1

def isPalindrome(x):
    if x < 0:
        return False
    return str(x) == str(x)[::-1]

# Example usage
x = 121
print("Is palindrome:", isPalindrome(x))  # Output: True
