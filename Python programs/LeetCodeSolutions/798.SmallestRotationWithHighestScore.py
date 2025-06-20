"""
798. Smallest Rotation with Highest Score

Given an array nums, we rotate the array k times. After each rotation, the score of the array is the number of indices i such that nums[i] <= i. Return the smallest k such that the score is maximized.

Example 1:
Input: nums = [2,3,1,4,0]
Output: 3

Example 2:
Input: nums = [1,3,0,2,4]
Output: 0

Constraints:
- 1 <= nums.length <= 10^5
- 0 <= nums[i] < nums.length
"""
def bestRotation(nums):
    n = len(nums)
    change = [0] * n
    for i, num in enumerate(nums):
        change[(i - num + 1) % n] -= 1
    score = 0
    max_score = 0
    res = 0
    for i in range(1, n):
        change[i] += change[i-1] + 1
        if change[i] > max_score:
            max_score = change[i]
            res = i
    return res

# Example usage:
print(bestRotation([2,3,1,4,0]))  # Output: 3
print(bestRotation([1,3,0,2,4]))  # Output: 0
