"""
LeetCode 1655. Distribute Repeating Integers

Given an array of integers and a list of quantity requirements, return true if it is possible to distribute the integers to satisfy all requirements.

Example 1:
Input: nums = [1,2,3,4], quantity = [2]
Output: false

Constraints:
- 1 <= nums.length <= 50
- 1 <= quantity.length <= 10
- 1 <= nums[i] <= 100
- 1 <= quantity[i] <= 50
"""

def canDistribute(nums, quantity):
    from collections import Counter
    count = list(Counter(nums).values())
    m = len(quantity)
    dp = {0: True}
    for c in count:
        ndp = dp.copy()
        for mask in dp:
            for sub in range(1, 1<<m):
                if bin(sub).count('1') > c:
                    continue
                if mask & sub:
                    continue
                total = 0
                for i in range(m):
                    if sub & (1<<i):
                        total += quantity[i]
                if total <= c:
                    ndp[mask|sub] = True
        dp = ndp
    return (1<<m)-1 in dp

# Example usage:
# nums = [1,2,3,4]
# quantity = [2]
# print(canDistribute(nums, quantity))  # Output: False
