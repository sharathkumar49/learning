"""
LeetCode 1646. Get Maximum in Generated Array

Given an integer n, return the maximum integer in the generated array nums defined as:
- nums[0] = 0
- nums[1] = 1
- nums[2*i] = nums[i]
- nums[2*i+1] = nums[i] + nums[i+1] for 2 <= 2*i+1 <= n

Example 1:
Input: n = 7
Output: 3

Constraints:
- 0 <= n <= 100
"""

def getMaximumGenerated(n):
    if n == 0:
        return 0
    nums = [0, 1] + [0]*(n-1)
    for i in range(2, n+1):
        if i % 2 == 0:
            nums[i] = nums[i//2]
        else:
            nums[i] = nums[i//2] + nums[i//2+1]
    return max(nums)

# Example usage:
# n = 7
# print(getMaximumGenerated(n))  # Output: 3
