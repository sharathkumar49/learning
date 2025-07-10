"""
LeetCode 2195. Append K Integers With Minimal Sum

Given an array nums and an integer k, append k unique positive integers not present in nums such that the sum is minimized. Return the sum.

Example:
Input: nums = [1,4,25,10,25], k = 2
Output: 5

Constraints:
- 1 <= nums.length <= 10^5
- 1 <= k <= 10^8
- 1 <= nums[i] <= 10^9
"""

def minimalKSum(nums, k):
    nums = sorted(set(nums))
    res, cur = 0, 1
    for x in nums:
        if x > cur:
            cnt = min(x-cur, k)
            res += (cur+cur+cnt-1)*cnt//2
            k -= cnt
            if k == 0:
                return res
        cur = x+1
    if k:
        res += (cur+cur+k-1)*k//2
    return res

# Example usage:
# print(minimalKSum([1,4,25,10,25], 2))  # Output: 5
