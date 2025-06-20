"""
LeetCode 673. Number of Longest Increasing Subsequence

Given an integer array nums, return the number of longest increasing subsequences.

Notice that the sequence has to be strictly increasing.

Example 1:
Input: nums = [1,3,5,4,7]
Output: 2
Explanation: The two longest increasing subsequence are [1,3,4,7] and [1,3,5,7].

Example 2:
Input: nums = [2,2,2,2,2]
Output: 5
Explanation: The length of longest increasing subsequence is 1, and there are 5 subsequences of length 1.

Constraints:
- 1 <= nums.length <= 2000
- -10^6 <= nums[i] <= 10^6
"""
from typing import List

def findNumberOfLIS(nums: List[int]) -> int:
    n = len(nums)
    if n == 0:
        return 0
    lengths = [1] * n
    counts = [1] * n
    for i in range(n):
        for j in range(i):
            if nums[i] > nums[j]:
                if lengths[j] + 1 > lengths[i]:
                    lengths[i] = lengths[j] + 1
                    counts[i] = counts[j]
                elif lengths[j] + 1 == lengths[i]:
                    counts[i] += counts[j]
    longest = max(lengths)
    return sum(c for l, c in zip(lengths, counts) if l == longest)

# Example usage
if __name__ == "__main__":
    print(findNumberOfLIS([1,3,5,4,7]))  # Output: 2
    print(findNumberOfLIS([2,2,2,2,2]))  # Output: 5
