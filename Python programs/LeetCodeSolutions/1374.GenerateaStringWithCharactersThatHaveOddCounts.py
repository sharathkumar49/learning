"""
LeetCode 1374. Generate a String With Characters That Have Odd Counts

Given an integer n, return a string with n characters such that every character appears an odd number of times.

Constraints:
- 1 <= n <= 1000

Example:
Input: n = 4
Output: "pppz"
"""
def generateTheString(n):
    if n % 2:
        return 'a' * n
    else:
        return 'a' * (n-1) + 'b'

# Example usage:
n = 4
print(generateTheString(n))  # Output: "aaab"
