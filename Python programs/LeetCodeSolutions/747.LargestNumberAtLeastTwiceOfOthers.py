"""
LeetCode 747. Largest Number At Least Twice of Others

You are given an integer array nums where the largest element is at least twice as much as every other number in the array.
Return the index of the largest element, or -1 if no such element exists.

Example 1:
Input: nums = [3,6,1,0]
Output: 1

Example 2:
Input: nums = [1,2,3,4]
Output: -1

Constraints:
- 1 <= nums.length <= 50
- 0 <= nums[i] <= 100
"""
from typing import List

def dominantIndex(nums: List[int]) -> int:
    m = max(nums)
    idx = nums.index(m)
    for i, n in enumerate(nums):
        if i != idx and m < 2 * n:
            return -1
    return idx

# Example usage
if __name__ == "__main__":
    print(dominantIndex([3,6,1,0]))  # Output: 1
    print(dominantIndex([1,2,3,4]))  # Output: -1
