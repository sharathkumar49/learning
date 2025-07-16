"""
LeetCode 2310. Sum of Numbers With Units Digit K

Given num and k, return the minimum number of positive integers whose sum is num and each has units digit k.

Example:
Input: num = 58, k = 9
Output: 2

Constraints:
- 1 <= num, k <= 100
"""

def minimumNumbers(num, k):
    if num == 0:
        return 0
    for i in range(1, 11):
        if num - k*i >= 0 and (num - k*i) % 10 == 0:
            return i
    return -1

# Example usage:
# print(minimumNumbers(58, 9))  # Output: 2
