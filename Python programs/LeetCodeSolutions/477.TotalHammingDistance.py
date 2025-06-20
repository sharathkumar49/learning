"""
477. Total Hamming Distance

Given an integer array nums, return the sum of Hamming distances between all the pairs of the integers in the array.

Constraints:
- 1 <= nums.length <= 10^4
- 0 <= nums[i] <= 10^9

Example:
Input: nums = [4,14,2]
Output: 6
"""

class Solution:
    def totalHammingDistance(self, nums: list) -> int:
        res = 0
        n = len(nums)
        for i in range(32):
            ones = sum((num >> i) & 1 for num in nums)
            res += ones * (n - ones)
        return res

# Example usage:
sol = Solution()
print(sol.totalHammingDistance([4,14,2]))  # Output: 6
