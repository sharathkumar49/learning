"""
LeetCode 2362. Generate the String With Given Character Counts

Given n, return a string with n characters such that the number of 'a's is odd.

Example:
Input: n = 4
Output: "aaab"

Constraints:
- 1 <= n <= 100
"""

def generateTheString(n):
    return 'a'*n if n%2 else 'a'*(n-1)+'b'

# Example usage:
# print(generateTheString(4))  # Output: "aaab"
