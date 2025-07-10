"""
LeetCode 1774. Closest Dessert Cost

Given arrays baseCosts and toppingCosts, and an integer target, return the closest cost to target for a dessert.

Example 1:
Input: baseCosts = [1,7], toppingCosts = [3,4], target = 10
Output: 10

Constraints:
- 1 <= baseCosts.length, toppingCosts.length <= 10
- 1 <= baseCosts[i], toppingCosts[i] <= 10^4
- 1 <= target <= 10^4
"""

def closestCost(baseCosts, toppingCosts, target):
    res = min(baseCosts)
    best = abs(res - target)
    possible = set(baseCosts)
    for t in toppingCosts:
        new = set()
        for x in possible:
            for cnt in range(3):
                new.add(x + t * cnt)
        possible = new
    for x in possible:
        if abs(x - target) < best or (abs(x - target) == best and x < res):
            res = x
            best = abs(x - target)
    return res

# Example usage:
# baseCosts = [1,7]
# toppingCosts = [3,4]
# target = 10
# print(closestCost(baseCosts, toppingCosts, target))  # Output: 10
