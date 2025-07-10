"""
LeetCode 2202. Maximize the Topmost Element After K Moves

Given an array nums and an integer k, in one move you can remove the first element and place it at the end or remove it entirely. Return the maximum possible value of the topmost element after k moves, or -1 if the array becomes empty.

Example:
Input: nums = [5,2,2,4,0,6], k = 4
Output: 4

Constraints:
- 1 <= nums.length <= 10^5
- 0 <= nums[i], k <= 10^9
"""

def maximumTop(nums, k):
    n = len(nums)
    if n == 1:
        return nums[0] if k % 2 == 0 else -1
    if k == 0:
        return nums[0]
    if k > n:
        return max(nums)
    max_val = max(nums[:k-1], default=-1)
    return max(max_val, nums[k] if k < n else -1)

# Example usage:
# print(maximumTop([5,2,2,4,0,6], 4))  # Output: 4
