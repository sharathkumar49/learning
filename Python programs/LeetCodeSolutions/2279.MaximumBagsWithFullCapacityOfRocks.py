"""
LeetCode 2279. Maximum Bags With Full Capacity of Rocks

Given capacity, rocks, and additionalRocks, return the maximum number of bags that can be filled.

Example:
Input: capacity = [2,3,4,5], rocks = [1,2,4,4], additionalRocks = 2
Output: 3

Constraints:
- 1 <= capacity.length == rocks.length <= 10^5
- 1 <= additionalRocks <= 10^9
"""

def maximumBags(capacity, rocks, additionalRocks):
    need = [c-r for c, r in zip(capacity, rocks)]
    need.sort()
    res = 0
    for n in need:
        if additionalRocks >= n:
            additionalRocks -= n
            res += 1
        else:
            break
    return res

# Example usage:
# print(maximumBags([2,3,4,5], [1,2,4,4], 2))  # Output: 3
