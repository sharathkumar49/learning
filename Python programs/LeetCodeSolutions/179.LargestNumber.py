"""
179. Largest Number
https://leetcode.com/problems/largest-number/

Given a list of non-negative integers nums, arrange them such that they form the largest number and return it.
Note: The result may be very large, so you need to return a string instead of an integer.

Constraints:
- 1 <= nums.length <= 100
- 0 <= nums[i] <= 10^9

Example 1:
Input: nums = [10,2]
Output: "210"

Example 2:
Input: nums = [3,30,34,5,9]
Output: "9534330"
"""
from functools import cmp_to_key

def largestNumber(nums):
    def compare(x, y):
        if x + y > y + x:
            return -1
        elif x + y < y + x:
            return 1
        else:
            return 0
    nums_str = list(map(str, nums))
    nums_str.sort(key=cmp_to_key(compare))
    result = ''.join(nums_str)
    return '0' if result[0] == '0' else result

# Example usage:
if __name__ == "__main__":
    print(largestNumber([10,2]))         # Output: "210"
    print(largestNumber([3,30,34,5,9])) # Output: "9534330"
