"""
LeetCode 2248. Intersection of Multiple Arrays

Given a list of arrays, return their intersection sorted in ascending order.

Example:
Input: nums = [[3,1,2,4,5],[1,2,3,4],[3,4,5,6]]
Output: [3,4]

Constraints:
- 1 <= nums.length <= 1000
- 1 <= nums[i].length <= 1000
"""

def intersection(nums):
    from functools import reduce
    return sorted(list(reduce(lambda a,b: set(a)&set(b), nums)))

# Example usage:
# print(intersection([[3,1,2,4,5],[1,2,3,4],[3,4,5,6]]))  # Output: [3,4]
