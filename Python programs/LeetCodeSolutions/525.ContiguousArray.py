"""
525. Contiguous Array

Given a binary array nums, return the maximum length of a contiguous subarray with an equal number of 0 and 1.

Constraints:
- 1 <= nums.length <= 10^5
- nums[i] is either 0 or 1.

Example:
Input: nums = [0,1]
Output: 2
"""

class Solution:
    def findMaxLength(self, nums: list) -> int:
        count = 0
        maxlen = 0
        d = {0: -1}
        for i, num in enumerate(nums):
            count += 1 if num == 1 else -1
            if count in d:
                maxlen = max(maxlen, i - d[count])
            else:
                d[count] = i
        return maxlen

# Example usage:
sol = Solution()
print(sol.findMaxLength([0,1]))  # Output: 2
