"""
209. Minimum Size Subarray Sum
https://leetcode.com/problems/minimum-size-subarray-sum/

Given an array of positive integers nums and a positive integer target, return the minimal length of a contiguous subarray [numsl, numsl+1, ..., numsr-1, numsr] of which the sum is greater than or equal to target. If there is no such subarray, return 0 instead.

Constraints:
- 1 <= target <= 10^9
- 1 <= nums.length <= 10^5
- 1 <= nums[i] <= 10^5

Example 1:
Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2

Example 2:
Input: target = 4, nums = [1,4,4]
Output: 1

Example 3:
Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0
"""
def minSubArrayLen(target, nums):
    n = len(nums)
    left = 0
    total = 0
    res = float('inf')
    for right in range(n):
        total += nums[right]
        while total >= target:
            res = min(res, right - left + 1)
            total -= nums[left]
            left += 1
    return 0 if res == float('inf') else res

# Example usage:
if __name__ == "__main__":
    print(minSubArrayLen(7, [2,3,1,2,4,3]))  # Output: 2
    print(minSubArrayLen(4, [1,4,4]))        # Output: 1
    print(minSubArrayLen(11, [1,1,1,1,1,1,1,1])) # Output: 0
