"""
LeetCode 1437. Check If All 1's Are at Least Length K Places Away

Given an array nums and an integer k, check if all 1's are at least k places away from each other.

Constraints:
- 1 <= nums.length <= 10^5
- 0 <= nums[i] <= 1
- 0 <= k <= nums.length

Example:
Input: nums = [1,0,0,0,1,0,0,1], k = 2
Output: true
"""
def kLengthApart(nums, k):
    prev = -k-1
    for i, n in enumerate(nums):
        if n == 1:
            if i - prev <= k:
                return False
            prev = i
    return True

# Example usage:
nums = [1,0,0,0,1,0,0,1]
k = 2
print(kLengthApart(nums, k))  # Output: True
