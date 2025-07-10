"""
LeetCode 1985. Find the Kth Largest Integer in the Array

Given an array nums of strings representing integers, return the kth largest integer in the array.

Example:
Input: nums = ["3","6","7","10"], k = 4
Output: "3"

Constraints:
- 1 <= k <= nums.length <= 10^4
- 1 <= nums[i].length <= 100
- nums[i] consists of only digits.
- nums[i] does not have leading zeros.
"""

def kthLargestNumber(nums, k):
    nums.sort(key=lambda x: (len(x), x))
    return nums[-k]

# Example usage:
# print(kthLargestNumber(["3","6","7","10"], 4))  # Output: "3"
