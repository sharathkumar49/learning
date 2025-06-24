"""
LeetCode 1424. Diagonal Traverse II

Given a list of lists of integers nums, return all elements of nums in diagonal order as shown in the problem statement.

Constraints:
- 1 <= nums.length <= 10^5
- 1 <= nums[i].length <= 10^5
- 1 <= sum(nums[i].length) <= 10^5

Example:
Input: nums = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,4,2,7,5,3,8,6,9]
"""
def findDiagonalOrder(nums):
    from collections import defaultdict
    diagonals = defaultdict(list)
    for i, row in enumerate(nums):
        for j, val in enumerate(row):
            diagonals[i+j].append(val)
    res = []
    for k in sorted(diagonals.keys()):
        res.extend(diagonals[k][::-1])
    return res

# Example usage:
nums = [[1,2,3],[4,5,6],[7,8,9]]
print(findDiagonalOrder(nums))  # Output: [1,4,2,7,5,3,8,6,9]
