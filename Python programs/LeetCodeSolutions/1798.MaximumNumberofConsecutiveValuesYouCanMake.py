"""
LeetCode 1798. Maximum Number of Consecutive Values You Can Make

Given an array coins, return the maximum number of consecutive values you can make starting from 0.

Example 1:
Input: coins = [1,3]
Output: 2

Constraints:
- 1 <= coins.length <= 10^5
- 1 <= coins[i] <= 10^4
"""

def getMaximumConsecutive(coins):
    coins.sort()
    res = 1
    for c in coins:
        if c > res:
            break
        res += c
    return res

# Example usage:
# coins = [1,3]
# print(getMaximumConsecutive(coins))  # Output: 2
