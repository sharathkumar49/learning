"""
LeetCode 2233. Maximum Product After K Increments

Given nums and k, return the maximum product after k increments.

Example:
Input: nums = [1,2,3], k = 3
Output: 27

Constraints:
- 1 <= nums.length <= 10^5
- 0 <= k <= 10^9
- 1 <= nums[i] <= 10^6
"""

def maximumProduct(nums, k):
    import heapq
    heapq.heapify(nums)
    for _ in range(k):
        heapq.heapreplace(nums, nums[0]+1)
    res = 1
    for num in nums:
        res = (res * num) % (10**9+7)
    return res

# Example usage:
# print(maximumProduct([1,2,3], 3))  # Output: 27
