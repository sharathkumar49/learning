"""
LeetCode 1716. Calculate Money in Leetcode Bank

Hercy wants to save money for his first car. Every Monday, he deposits a certain amount, and each day he deposits $1 more than the previous day. Return the total money after n days.

Example 1:
Input: n = 4
Output: 10

Constraints:
- 1 <= n <= 1000
"""

def totalMoney(n):
    weeks, days = divmod(n, 7)
    total = 28 * weeks + 7 * weeks * (weeks - 1) // 2
    for i in range(days):
        total += weeks + 1 + i
    return total

# Example usage:
# n = 4
# print(totalMoney(n))  # Output: 10
