"""
LeetCode 2240. Number of Ways to Buy Pens and Pencils

Given total, cost1, cost2, return the number of ways to buy pens and pencils.

Example:
Input: total = 20, cost1 = 10, cost2 = 5
Output: 9

Constraints:
- 1 <= total, cost1, cost2 <= 10^6
"""

def waysToBuyPensPencils(total, cost1, cost2):
    res = 0
    for i in range(total//cost1+1):
        res += (total - i*cost1)//cost2 + 1
    return res

# Example usage:
# print(waysToBuyPensPencils(20, 10, 5))  # Output: 9
