"""
LeetCode 1674. Minimum Moves to Make Array Complementary

Given an array nums and an integer limit, return the minimum number of moves to make every pair (nums[i], nums[n-1-i]) sum to the same value.

Example 1:
Input: nums = [1,2,4,3], limit = 4
Output: 1

Constraints:
- 1 <= nums.length <= 10^5
- 1 <= limit <= 10^5
- 1 <= nums[i] <= limit
"""

def minMoves(nums, limit):
    n = len(nums)
    diff = [0]*(2*limit+2)
    for i in range(n//2):
        a, b = nums[i], nums[n-1-i]
        diff[2] += 2
        diff[min(a, b)+1] -= 1
        diff[a+b] -= 1
        diff[a+b+1] += 1
        diff[max(a, b)+limit+1] += 1
    res = n
    curr = 0
    for i in range(2, 2*limit+1):
        curr += diff[i]
        res = min(res, curr)
    return res

# Example usage:
# nums = [1,2,4,3]
# limit = 4
# print(minMoves(nums, limit))  # Output: 1
