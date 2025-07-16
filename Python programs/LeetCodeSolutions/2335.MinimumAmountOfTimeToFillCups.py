"""
LeetCode 2335. Minimum Amount of Time to Fill Cups

Given amount, return the minimum time to fill all cups.

Example:
Input: amount = [1,4,2]
Output: 4

Constraints:
- amount.length == 3
- 0 <= amount[i] <= 100
"""

def fillCups(amount):
    amount.sort()
    if amount[2] > amount[0]+amount[1]:
        return amount[2]
    return (sum(amount)+1)//2

# Example usage:
# print(fillCups([1,4,2]))  # Output: 4
