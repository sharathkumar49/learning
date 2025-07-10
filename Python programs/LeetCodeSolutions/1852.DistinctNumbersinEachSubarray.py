"""
LeetCode 1852. Distinct Numbers in Each Subarray

Given an integer array nums and an integer k, return an array of the number of distinct elements in every contiguous subarray of size k.

Example 1:
Input: nums = [1,2,3,2,2,1,3], k = 3
Output: [3,2,2,2,3]

Constraints:
- 1 <= k <= nums.length <= 10^5
- 1 <= nums[i] <= 10^5
"""

def distinctNumbers(nums, k):
    from collections import defaultdict
    count = defaultdict(int)
    res = []
    for i in range(len(nums)):
        count[nums[i]] += 1
        if i >= k:
            count[nums[i-k]] -= 1
            if count[nums[i-k]] == 0:
                del count[nums[i-k]]
        if i >= k-1:
            res.append(len(count))
    return res

# Example usage:
# nums = [1,2,3,2,2,1,3]
# k = 3
# print(distinctNumbers(nums, k))  # Output: [3,2,2,2,3]
