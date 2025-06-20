"""
493. Reverse Pairs

Given an integer array nums, return the number of reverse pairs in the array. A reverse pair is a pair (i, j) where 0 <= i < j < nums.length and nums[i] > 2*nums[j].

Constraints:
- 1 <= nums.length <= 5 * 10^4
- -2^31 <= nums[i] <= 2^31 - 1

Example:
Input: nums = [1,3,2,3,1]
Output: 2
"""

class Solution:
    def reversePairs(self, nums: list) -> int:
        def merge_sort(l, r):
            if l >= r:
                return 0
            m = (l + r) // 2
            count = merge_sort(l, m) + merge_sort(m+1, r)
            j = m + 1
            for i in range(l, m+1):
                while j <= r and nums[i] > 2 * nums[j]:
                    j += 1
                count += j - (m + 1)
            nums[l:r+1] = sorted(nums[l:r+1])
            return count
        return merge_sort(0, len(nums)-1)

# Example usage:
sol = Solution()
print(sol.reversePairs([1,3,2,3,1]))  # Output: 2
