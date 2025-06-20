"""
152. Maximum Product Subarray
https://leetcode.com/problems/maximum-product-subarray/

Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.

Constraints:
- 1 <= nums.length <= 2 * 10^4
- -10 <= nums[i] <= 10

Example:
Input: nums = [2,3,-2,4]
Output: 6
"""
from typing import List

def maxProduct(nums: List[int]) -> int:
    if not nums:
        return 0
    max_prod = min_prod = result = nums[0]
    for n in nums[1:]:
        candidates = (n, max_prod * n, min_prod * n)
        max_prod = max(candidates)
        min_prod = min(candidates)
        result = max(result, max_prod)
    return result

# Example usage:
if __name__ == "__main__":
    print(maxProduct([2,3,-2,4]))  # Output: 6
    print(maxProduct([-2,0,-1]))   # Output: 0
