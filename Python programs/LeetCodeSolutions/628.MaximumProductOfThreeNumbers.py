"""
628. Maximum Product of Three Numbers
Difficulty: Easy

Given an integer array nums, find three numbers whose product is maximum and return the maximum product.

Example 1:
Input: nums = [1,2,3]
Output: 6

Example 2:
Input: nums = [1,2,3,4]
Output: 24

Constraints:
3 <= nums.length <= 10^4
-1000 <= nums[i] <= 1000
"""

def maximumProduct(nums):
    nums.sort()
    return max(nums[-1]*nums[-2]*nums[-3], nums[0]*nums[1]*nums[-1])

# Example usage
if __name__ == "__main__":
    print(maximumProduct([1,2,3]))    # Output: 6
    print(maximumProduct([1,2,3,4]))  # Output: 24
