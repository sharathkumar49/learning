"""
LeetCode 1313. Decompress Run-Length Encoded List

Given a list nums, decompress it as follows: for each pair [freq, val], output freq copies of val. Return the decompressed list.

Constraints:
- 2 <= nums.length <= 100
- nums.length % 2 == 0
- 1 <= nums[i] <= 100

Example:
Input: nums = [1,2,3,4]
Output: [2,4,4,4]
"""
def decompressRLElist(nums):
    res = []
    for i in range(0, len(nums), 2):
        res += [nums[i+1]] * nums[i]
    return res

# Example usage:
nums = [1,2,3,4]
print(decompressRLElist(nums))  # Output: [2,4,4,4]
