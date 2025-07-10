"""
LeetCode 1616. Split Two Strings to Make Palindrome

Given two strings a and b, return true if you can split both strings at some index and join one prefix with the other suffix to make a palindrome.

Example 1:
Input: a = "x", b = "y"
Output: true

Constraints:
- 1 <= a.length, b.length <= 10^5
- a.length == b.length
- a and b consist of lowercase English letters.
"""

def checkPalindromeFormation(a, b):
    def check(x, y):
        l, r = 0, len(x)-1
        while l < r and x[l] == y[r]:
            l += 1
            r -= 1
        s = x[l:r+1]
        return s == s[::-1]
    return check(a, b) or check(b, a)

# Example usage:
# a = "x"
# b = "y"
# print(checkPalindromeFormation(a, b))  # Output: True
