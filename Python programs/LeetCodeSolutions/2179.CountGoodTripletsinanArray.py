"""
LeetCode 2179. Count Good Triplets in an Array

Given an array nums and an integer k, return the number of good triplets (i, j, l) such that 0 <= i < j < l < n, nums[i] == nums[j] == nums[l], and (i * j * l) is divisible by k.

Example:
Input: nums = [1,2,1,2,1,2,1], k = 1
Output: 5

Constraints:
- 3 <= nums.length <= 100
- 1 <= nums[i], k <= 100
"""

def countGoodTriplets(nums, k):
    res = 0
    n = len(nums)
    for i in range(n):
        for j in range(i+1, n):
            for l in range(j+1, n):
                if nums[i] == nums[j] == nums[l] and (i*j*l)%k == 0:
                    res += 1
    return res

# Example usage:
# print(countGoodTriplets([1,2,1,2,1,2,1], 1))  # Output: 5
