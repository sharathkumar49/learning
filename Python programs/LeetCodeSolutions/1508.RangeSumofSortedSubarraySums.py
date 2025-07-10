"""
LeetCode 1508. Range Sum of Sorted Subarray Sums

Given an integer array nums, return the sum of the sorted subarray sums from left to right indices (1-indexed).

Constraints:
- 1 <= nums.length <= 1000
- 1 <= nums[i] <= 100
- 1 <= left <= right <= n * (n + 1) / 2

Example:
Input: nums = [1,2,3,4], n = 4, left = 1, right = 5
Output: 13
"""
def rangeSum(nums, n, left, right):
    sub = []
    for i in range(n):
        s = 0
        for j in range(i, n):
            s += nums[j]
            sub.append(s)
    sub.sort()
    return sum(sub[left-1:right]) % (10**9+7)

# Example usage:
nums = [1,2,3,4]
n = 4
left = 1
right = 5
print(rangeSum(nums, n, left, right))  # Output: 13
