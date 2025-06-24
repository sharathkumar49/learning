"""
LeetCode 1281. Subtract the Product and Sum of Digits of an Integer

Given an integer n, return the difference between the product of its digits and the sum of its digits.

Constraints:
- 1 <= n <= 10^5

Example:
Input: n = 234
Output: 15
"""
def subtractProductAndSum(n):
    s = str(n)
    prod = 1
    summ = 0
    for c in s:
        prod *= int(c)
        summ += int(c)
    return prod - summ

# Example usage:
print(subtractProductAndSum(234))  # Output: 15
