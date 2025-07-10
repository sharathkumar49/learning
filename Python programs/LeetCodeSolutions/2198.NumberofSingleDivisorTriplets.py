"""
LeetCode 2198. Number of Single Divisor Triplets

Given an array nums, return the number of triplets (i, j, k) such that i < j < k and (nums[i] + nums[j] + nums[k]) is divisible by exactly one of nums[i], nums[j], or nums[k].

Example:
Input: nums = [4,6,7,8,10]
Output: 5

Constraints:
- 3 <= nums.length <= 100
- 1 <= nums[i] <= 10^4
"""

def singleDivisorTriplet(nums):
    n = len(nums)
    res = 0
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                s = nums[i]+nums[j]+nums[k]
                cnt = sum(s%x==0 for x in [nums[i],nums[j],nums[k]])
                if cnt == 1:
                    res += 1
    return res

# Example usage:
# print(singleDivisorTriplet([4,6,7,8,10]))  # Output: 5
