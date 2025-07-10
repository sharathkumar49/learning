"""
LeetCode 1833. Maximum Ice Cream Bars

Given an array costs and an integer coins, return the maximum number of ice cream bars you can buy.

Example 1:
Input: costs = [1,3,2,4,1], coins = 7
Output: 4

Constraints:
- 1 <= costs.length <= 10^5
- 1 <= costs[i] <= 10^5
- 1 <= coins <= 10^8
"""

def maxIceCream(costs, coins):
    costs.sort()
    res = 0
    for c in costs:
        if coins < c:
            break
        coins -= c
        res += 1
    return res

# Example usage:
# costs = [1,3,2,4,1]
# coins = 7
# print(maxIceCream(costs, coins))  # Output: 4
