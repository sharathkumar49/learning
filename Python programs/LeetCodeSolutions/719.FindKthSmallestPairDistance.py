"""
LeetCode 719. Find K-th Smallest Pair Distance

Given an integer array nums and an integer k, return the k-th smallest distance among all the pairs. The distance of a pair (A, B) is |A - B|.

Example 1:
Input: nums = [1,3,1], k = 1
Output: 0

Example 2:
Input: nums = [1,6,1], k = 3
Output: 5

Constraints:
- n == nums.length
- 2 <= n <= 10^4
- 0 <= nums[i] < 10^6
- 1 <= k <= n * (n - 1) / 2
"""
from typing import List

def smallestDistancePair(nums: List[int], k: int) -> int:
    nums.sort()
    n = len(nums)
    def count(mid):
        cnt = left = 0
        for right in range(n):
            while nums[right] - nums[left] > mid:
                left += 1
            cnt += right - left
        return cnt
    left, right = 0, nums[-1] - nums[0]
    while left < right:
        mid = (left + right) // 2
        if count(mid) < k:
            left = mid + 1
        else:
            right = mid
    return left

# Example usage
if __name__ == "__main__":
    print(smallestDistancePair([1,3,1], 1))  # Output: 0
    print(smallestDistancePair([1,6,1], 3))  # Output: 5
