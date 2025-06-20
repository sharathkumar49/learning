"""
128. Longest Consecutive Sequence
https://leetcode.com/problems/longest-consecutive-sequence/

Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
You must write an algorithm that runs in O(n) time.

Constraints:
- 0 <= nums.length <= 10^5
- -10^9 <= nums[i] <= 10^9

Example:
Input: nums = [100,4,200,1,3,2]
Output: 4
"""
from typing import List

def longestConsecutive(nums: List[int]) -> int:
    num_set = set(nums)
    longest = 0
    for n in num_set:
        if n - 1 not in num_set:
            length = 1
            while n + length in num_set:
                length += 1
            longest = max(longest, length)
    return longest

# Example usage:
if __name__ == "__main__":
    print(longestConsecutive([100,4,200,1,3,2]))  # Output: 4
    print(longestConsecutive([]))                 # Output: 0
