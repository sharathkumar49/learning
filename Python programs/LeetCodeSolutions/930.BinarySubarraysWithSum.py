"""
930. Binary Subarrays With Sum
https://leetcode.com/problems/binary-subarrays-with-sum/

Given a binary array nums and an integer goal, return the number of non-empty subarrays with a sum equal to goal.

Constraints:
- 1 <= nums.length <= 3 * 10^4
- nums[i] is 0 or 1
- 0 <= goal <= nums.length

Example:
Input: nums = [1,0,1,0,1], goal = 2
Output: 4
"""
from typing import List

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        from collections import defaultdict
        count = defaultdict(int)
        count[0] = 1
        res = s = 0
        for x in nums:
            s += x
            res += count[s - goal]
            count[s] += 1
        return res

# Example usage
if __name__ == "__main__":
    nums = [1,0,1,0,1]
    goal = 2
    print(Solution().numSubarraysWithSum(nums, goal))  # Output: 4
