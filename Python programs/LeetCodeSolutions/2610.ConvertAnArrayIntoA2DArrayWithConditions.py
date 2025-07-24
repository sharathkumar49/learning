"""
LeetCode 2610. Convert an Array Into a 2D Array With Conditions

Given nums, return a 2D array with conditions.

Constraints:
- 1 <= nums.length <= 200
"""

def findMatrix(nums):
    from collections import Counter
    c = Counter(nums)
    res = []
    while c:
        row = []
        for x in list(c):
            row.append(x)
            c[x] -= 1
            if c[x] == 0:
                del c[x]
        res.append(row)
    return res
# Example usage:
# print(findMatrix([1,3,4,1,2,3,1]))  # Output: [[1,2,3,4],[1,3],[1]]
