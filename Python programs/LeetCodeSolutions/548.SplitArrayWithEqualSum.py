"""
548. Split Array with Equal Sum

Given an integer array nums, split it into four non-overlapping subarrays such that the sum of the subarrays is equal. Return true if possible, otherwise false.

Constraints:
- 1 <= nums.length <= 2000
- -10^6 <= nums[i] <= 10^6

Example:
Input: nums = [1,2,1,2,1,2,1]
Output: true
"""

class Solution:
    def splitArray(self, nums: list) -> bool:
        n = len(nums)
        if n < 7:
            return False
        prefix = [0] * n
        prefix[0] = nums[0]
        for i in range(1, n):
            prefix[i] = prefix[i-1] + nums[i]
        for j in range(3, n-3):
            seen = set()
            for i in range(1, j-1):
                if prefix[i-1] == prefix[j-1] - prefix[i] :
                    seen.add(prefix[i-1])
            for k in range(j+2, n-1):
                if prefix[k-1] - prefix[j] == prefix[n-1] - prefix[k] and prefix[k-1] - prefix[j] in seen:
                    return True
        return False

# Example usage:
sol = Solution()
print(sol.splitArray([1,2,1,2,1,2,1]))  # Output: True
