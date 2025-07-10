"""
LeetCode 1980. Find Unique Binary String

Given an array of n unique binary strings, return a binary string of length n that does not appear in the array.

Example:
Input: nums = ["01","10"]
Output: "00"

Constraints:
- n == nums.length
- 1 <= n <= 16
- nums[i].length == n
- nums[i] consists of '0' or '1'.
"""

def findDifferentBinaryString(nums):
    n = len(nums)
    s = set(nums)
    for i in range(2**n):
        b = bin(i)[2:].zfill(n)
        if b not in s:
            return b

# Example usage:
# print(findDifferentBinaryString(["01","10"]))  # Output: "00"
