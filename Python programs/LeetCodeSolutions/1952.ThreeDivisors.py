"""
LeetCode 1952. Three Divisors

Given an integer n, return true if n has exactly three positive divisors, otherwise false.

Example:
Input: n = 2
Output: false

Constraints:
- 1 <= n <= 10^4
"""

def isThree(n):
    cnt = 0
    for i in range(1, n+1):
        if n % i == 0:
            cnt += 1
    return cnt == 3

# Example usage:
# print(isThree(2))  # Output: False
