"""
LeetCode 1403. Minimum Subsequence in Non-Increasing Order

Given the array nums, return the minimum subsequence in non-increasing order such that the sum of the subsequence is strictly greater than the sum of the elements not included.

Constraints:
- 1 <= nums.length <= 500
- 1 <= nums[i] <= 100

Example:
Input: nums = [4,3,10,9,8]
Output: [10,9]
"""
def minSubsequence(nums):
    nums.sort(reverse=True)
    total = sum(nums)
    curr = 0
    res = []
    for n in nums:
        curr += n
        res.append(n)
        if curr > total - curr:
            break
    return res

# Example usage:
nums = [4,3,10,9,8]
print(minSubsequence(nums))  # Output: [10, 9]
