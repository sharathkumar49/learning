"""
829. Consecutive Numbers Sum

Given an integer n, return the number of ways you can write n as the sum of consecutive positive integers.

Example 1:
Input: n = 5
Output: 2

Example 2:
Input: n = 9
Output: 3

Constraints:
- 1 <= n <= 10^9
"""
def consecutiveNumbersSum(n):
    ans = 0
    k = 1
    while k * (k - 1) // 2 < n:
        if (n - k * (k - 1) // 2) % k == 0:
            ans += 1
        k += 1
    return ans

# Example usage:
print(consecutiveNumbersSum(5))  # Output: 2
print(consecutiveNumbersSum(9))  # Output: 3
