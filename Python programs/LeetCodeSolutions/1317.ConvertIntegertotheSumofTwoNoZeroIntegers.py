"""
LeetCode 1317. Convert Integer to the Sum of Two No-Zero Integers

Given an integer n, return two integers whose sum is n and neither contains the digit zero.

Constraints:
- 2 <= n <= 10^4

Example:
Input: n = 11
Output: [2,9]
"""
def getNoZeroIntegers(n):
    def hasZero(x):
        return '0' in str(x)
    for a in range(1, n):
        b = n - a
        if not hasZero(a) and not hasZero(b):
            return [a, b]

# Example usage:
n = 11
print(getNoZeroIntegers(n))  # Output: [2, 9]
