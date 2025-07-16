"""
LeetCode 2367. Number of Arithmetic Triplets

Given nums and diff, return the number of arithmetic triplets.

Example:
Input: nums = [0,1,4,6,7,10], diff = 3
Output: 2

Constraints:
- 3 <= nums.length <= 200
- 0 <= nums[i] <= 200
"""

def arithmeticTriplets(nums, diff):
    s = set(nums)
    return sum((x+diff in s and x+2*diff in s) for x in nums)

# Example usage:
# print(arithmeticTriplets([0,1,4,6,7,10], 3))  # Output: 2
