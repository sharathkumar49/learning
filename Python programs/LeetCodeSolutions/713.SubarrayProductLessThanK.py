"""
LeetCode 713. Subarray Product Less Than K

Given an array of positive integers nums and an integer k, return the number of contiguous subarrays where the product of all the elements in the subarray is strictly less than k.

Example 1:
Input: nums = [10,5,2,6], k = 100
Output: 8

Example 2:
Input: nums = [1,2,3], k = 0
Output: 0

Constraints:
- 1 <= nums.length <= 3 * 10^4
- 1 <= nums[i] <= 1000
- 0 <= k <= 10^6
"""
from typing import List

def numSubarrayProductLessThanK(nums: List[int], k: int) -> int:
    if k <= 1:
        return 0
    prod = 1
    left = 0
    res = 0
    for right, val in enumerate(nums):
        prod *= val
        while prod >= k:
            prod //= nums[left]
            left += 1
        res += right - left + 1
    return res

# Example usage
if __name__ == "__main__":
    print(numSubarrayProductLessThanK([10,5,2,6], 100))  # Output: 8
    print(numSubarrayProductLessThanK([1,2,3], 0))       # Output: 0
