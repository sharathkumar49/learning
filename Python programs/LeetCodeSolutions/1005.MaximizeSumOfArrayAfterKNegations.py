"""
1005. Maximize Sum Of Array After K Negations

Given an integer array nums and an integer k, modify the array in the following way: choose an index i and replace nums[i] with -nums[i]. You should apply this process exactly k times. You may choose the same index i multiple times.

Return the largest possible sum of the array after modifying it in this way.

Example 1:
Input: nums = [4,2,3], k = 1
Output: 5
Explanation: Choose index 2 and nums becomes [4,2,-3].

Example 2:
Input: nums = [3,-1,0,2], k = 3
Output: 6

Example 3:
Input: nums = [2,-3,-1,5,-4], k = 2
Output: 13

Constraints:
- 1 <= nums.length <= 10^4
- 1 <= k <= 10^4
- -100 <= nums[i] <= 100
"""
from typing import List

def largestSumAfterKNegations(nums: List[int], k: int) -> int:
    nums.sort()
    for i in range(len(nums)):
        if k and nums[i] < 0:
            nums[i] = -nums[i]
            k -= 1
    if k % 2:
        nums.sort()
        nums[0] = -nums[0]
    return sum(nums)

# Example usage
if __name__ == "__main__":
    print(largestSumAfterKNegations([4,2,3], 1))      # Output: 5
    print(largestSumAfterKNegations([3,-1,0,2], 3))   # Output: 6
    print(largestSumAfterKNegations([2,-3,-1,5,-4], 2)) # Output: 13
