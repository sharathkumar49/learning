"""
LeetCode 1438. Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit

Given an array nums and an integer limit, return the size of the longest continuous subarray such that the absolute difference between any two elements is less than or equal to limit.

Constraints:
- 1 <= nums.length <= 10^5
- 1 <= nums[i] <= 10^9
- 0 <= limit <= 10^9

Example:
Input: nums = [8,2,4,7], limit = 4
Output: 2
"""
def longestSubarray(nums, limit):
    from collections import deque
    maxd, mind = deque(), deque()
    i = 0
    for j, n in enumerate(nums):
        while maxd and n > maxd[-1]: maxd.pop()
        while mind and n < mind[-1]: mind.pop()
        maxd.append(n)
        mind.append(n)
        if maxd[0] - mind[0] > limit:
            if maxd[0] == nums[i]: maxd.popleft()
            if mind[0] == nums[i]: mind.popleft()
            i += 1
    return len(nums) - i if i else len(nums)

# Example usage:
nums = [8,2,4,7]
limit = 4
print(longestSubarray(nums, limit))  # Output: 2
