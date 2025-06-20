"""
480. Sliding Window Median

Given an array nums and a sliding window of size k, return the median of each window as it slides from left to right.

Constraints:
- 1 <= k <= nums.length <= 10^5
- -2^31 <= nums[i] <= 2^31 - 1

Example:
Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [1, -1, -1, 3, 5, 6]
"""

import bisect

class Solution:
    def medianSlidingWindow(self, nums: list, k: int) -> list:
        window = sorted(nums[:k])
        medians = []
        for i in range(k, len(nums)+1):
            if k % 2:
                medians.append(window[k//2])
            else:
                medians.append((window[k//2-1] + window[k//2]) / 2)
            if i == len(nums):
                break
            window.remove(nums[i-k])
            bisect.insort(window, nums[i])
        return medians

# Example usage:
sol = Solution()
print(sol.medianSlidingWindow([1,3,-1,-3,5,3,6,7], 3))  # Output: [1, -1, -1, 3, 5, 6]
