"""
260. Single Number III
https://leetcode.com/problems/single-number-iii/

Given an integer array nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once. You can return the answer in any order.

Constraints:
- 2 <= nums.length <= 3 * 10^4
- -2^31 <= nums[i] <= 2^31 - 1
- Each integer in nums will appear twice, only two integers will appear once.

Example 1:
Input: nums = [1,2,1,3,2,5]
Output: [3,5]

Example 2:
Input: nums = [-1,0]
Output: [-1,0]

Example 3:
Input: nums = [0,1]
Output: [1,0]
"""
def singleNumber(nums):
    xor = 0
    for n in nums:
        xor ^= n
    diff = xor & -xor
    a = b = 0
    for n in nums:
        if n & diff:
            a ^= n
        else:
            b ^= n
    return [a, b]

# Example usage:
if __name__ == "__main__":
    print(sorted(singleNumber([1,2,1,3,2,5])))  # Output: [3,5]
    print(sorted(singleNumber([-1,0])))         # Output: [-1,0]
    print(sorted(singleNumber([0,1])))          # Output: [0,1]
