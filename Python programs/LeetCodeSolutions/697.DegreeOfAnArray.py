"""
LeetCode 697. Degree of an Array

Given a non-empty array of non-negative integers nums, the degree of this array is defined as the maximum frequency of any one of its elements.
Return the smallest possible length of a (contiguous) subarray of nums, that has the same degree as nums.

Example 1:
Input: nums = [1,2,2,3,1]
Output: 2

Example 2:
Input: nums = [1,2,2,3,1,4,2]
Output: 6

Constraints:
- 1 <= nums.length <= 50,000
- 0 <= nums[i] < 50,000
"""
from typing import List

def findShortestSubArray(nums: List[int]) -> int:
    left, right, count = {}, {}, {}
    for i, x in enumerate(nums):
        if x not in left:
            left[x] = i
        right[x] = i
        count[x] = count.get(x, 0) + 1
    degree = max(count.values())
    return min(right[x] - left[x] + 1 for x in count if count[x] == degree)

# Example usage
if __name__ == "__main__":
    print(findShortestSubArray([1,2,2,3,1]))      # Output: 2
    print(findShortestSubArray([1,2,2,3,1,4,2]))  # Output: 6
