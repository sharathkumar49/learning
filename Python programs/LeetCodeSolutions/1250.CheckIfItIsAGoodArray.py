"""
1250. Check If It Is a Good Array

Given an array nums, return True if it is a good array. An array is good if there exist x_i such that sum(x_i * nums[i]) = 1.

Constraints:
- 1 <= nums.length <= 10^5
- 1 <= nums[i] <= 10^9

Example:
Input: nums = [12,5,7,23]
Output: True

"""
def isGoodArray(nums):
    from math import gcd
    from functools import reduce
    return reduce(gcd, nums) == 1

# Example usage
if __name__ == "__main__":
    print(isGoodArray([12,5,7,23]))  # Output: True
