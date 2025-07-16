"""
LeetCode 2289. Steps to Make Array Non-Decreasing

Given nums, return the minimum number of steps to make the array non-decreasing.

Example:
Input: nums = [5,3,4,4,7,3,6,11,8,5,11]
Output: 3

Constraints:
- 1 <= nums.length <= 10^5
"""

def totalSteps(nums):
    stack = []
    res = [0]*len(nums)
    ans = 0
    for i in range(len(nums)-1, -1, -1):
        cnt = 0
        while stack and nums[i] > nums[stack[-1]]:
            cnt = max(cnt+1, res[stack.pop()])
        res[i] = cnt
        ans = max(ans, cnt)
        stack.append(i)
    return ans

# Example usage:
# print(totalSteps([5,3,4,4,7,3,6,11,8,5,11]))  # Output: 3
