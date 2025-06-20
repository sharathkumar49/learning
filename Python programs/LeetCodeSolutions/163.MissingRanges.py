"""
163. Missing Ranges
https://leetcode.com/problems/missing-ranges/

Given a sorted integer array nums, where the range of elements are in the inclusive range [lower, upper], return its missing ranges.

Constraints:
- -2^31 <= lower <= upper <= 2^31 - 1
- 0 <= nums.length <= 100

Example:
Input: nums = [0,1,3,50,75], lower = 0, upper = 99
Output: [[2,2],[4,49],[51,74],[76,99]]
"""
from typing import List

def findMissingRanges(nums: List[int], lower: int, upper: int) -> List[List[int]]:
    res = []
    prev = lower - 1
    nums.append(upper + 1)
    for num in nums:
        if num - prev == 2:
            res.append([prev + 1, prev + 1])
        elif num - prev > 2:
            res.append([prev + 1, num - 1])
        prev = num
    return res

# Example usage:
if __name__ == "__main__":
    print(findMissingRanges([0,1,3,50,75], 0, 99))  # Output: [[2,2],[4,49],[51,74],[76,99]]
