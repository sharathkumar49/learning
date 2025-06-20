"""
137. Single Number II
https://leetcode.com/problems/single-number-ii/

Given an integer array nums where every element appears three times except for one, which appears exactly once. Find the single one.

Constraints:
- 1 <= nums.length <= 3 * 10^4
- -2^31 <= nums[i] <= 2^31 - 1
- Each element in nums appears exactly three times except for one element which appears once.

Example:
Input: nums = [2,2,3,2]
Output: 3
"""
from typing import List

def singleNumber(nums: List[int]) -> int:
    ones, twos = 0, 0
    for num in nums:
        ones = (ones ^ num) & ~twos
        twos = (twos ^ num) & ~ones
    return ones

# Example usage:
if __name__ == "__main__":
    print(singleNumber([2,2,3,2]))  # Output: 3
    print(singleNumber([0,1,0,1,0,1,99]))  # Output: 99
