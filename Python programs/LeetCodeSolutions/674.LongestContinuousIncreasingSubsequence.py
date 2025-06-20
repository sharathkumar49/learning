"""
LeetCode 674. Longest Continuous Increasing Subsequence

Given an unsorted array of integers nums, return the length of the longest continuous increasing subsequence (i.e. subarray). The subsequence must be strictly increasing.

Example 1:
Input: nums = [1,3,5,4,7]
Output: 3
Explanation: The longest continuous increasing subsequence is [1,3,5] with length 3.

Example 2:
Input: nums = [2,2,2,2,2]
Output: 1

Constraints:
- 1 <= nums.length <= 10^4
- -10^9 <= nums[i] <= 10^9
"""
from typing import List

def findLengthOfLCIS(nums: List[int]) -> int:
    if not nums:
        return 0
    max_len = cur_len = 1
    for i in range(1, len(nums)):
        if nums[i] > nums[i-1]:
            cur_len += 1
            max_len = max(max_len, cur_len)
        else:
            cur_len = 1
    return max_len

# Example usage
if __name__ == "__main__":
    print(findLengthOfLCIS([1,3,5,4,7]))  # Output: 3
    print(findLengthOfLCIS([2,2,2,2,2]))  # Output: 1
