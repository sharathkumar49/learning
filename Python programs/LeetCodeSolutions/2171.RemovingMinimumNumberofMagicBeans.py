"""
LeetCode 2171. Removing Minimum Number of Magic Beans

Given an array beans, return the minimum number of beans to remove so that all non-empty bags have the same number of beans.

Example:
Input: beans = [4,3,6,6,2]
Output: 4

Constraints:
- 1 <= beans.length <= 10^5
- 1 <= beans[i] <= 10^5
"""

def minimumRemoval(beans):
    beans.sort()
    total = sum(beans)
    res = total
    n = len(beans)
    for i, b in enumerate(beans):
        res = min(res, total - b*(n-i))
    return res

# Example usage:
# print(minimumRemoval([4,3,6,6,2]))  # Output: 4
