"""
LeetCode 1703. Minimum Adjacent Swaps for K Consecutive Ones

Given a binary array nums and an integer k, return the minimum number of adjacent swaps required to get k consecutive 1's in the array.

Example 1:
Input: nums = [1,0,0,1,0,1], k = 2
Output: 1

Constraints:
- 1 <= nums.length <= 10^5
- nums[i] is 0 or 1
- 1 <= k <= sum(nums)
"""

def minMoves(nums, k):
    ones = [i for i, v in enumerate(nums) if v == 1]
    prefix = [0]
    for x in ones:
        prefix.append(prefix[-1] + x)
    res = float('inf')
    for i in range(len(ones) - k + 1):
        mid = i + k // 2
        median = ones[mid]
        left = prefix[mid] - prefix[i]
        right = prefix[i + k] - prefix[mid + 1]
        res = min(res, (median * (mid - i) - left) + (right - median * (i + k - mid - 1)))
    return res

# Example usage:
# nums = [1,0,0,1,0,1], k = 2
# print(minMoves(nums, k))  # Output: 1
