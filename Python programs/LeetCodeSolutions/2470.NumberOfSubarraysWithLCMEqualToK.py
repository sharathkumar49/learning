"""
LeetCode 2470. Number of Subarrays With LCM Equal to K

Given an array and k, return the number of subarrays with LCM equal to k.

Constraints:
- 1 <= nums.length <= 1000
- 1 <= k <= 10^9
"""

def subarrayLCM(nums, k):
    from math import lcm
    res = 0
    for i in range(len(nums)):
        curr = 1
        for j in range(i, len(nums)):
            curr = lcm(curr, nums[j])
            if curr == k:
                res += 1
            if curr > k:
                break
    return res

# Example usage:
# print(subarrayLCM([3,6,2,7,1], 6))  # Output: 4
