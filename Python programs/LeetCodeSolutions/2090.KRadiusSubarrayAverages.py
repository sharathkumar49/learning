"""
LeetCode 2090. K Radius Subarray Averages

Given an array nums and an integer k, return an array of the averages of each subarray of length 2k+1 centered at each index, or -1 if not enough elements.

Example:
Input: nums = [7,4,3,9,1,8,5,2,6], k = 3
Output: [-1,-1,-1,5,4,4,-1,-1,-1]

Constraints:
- 1 <= nums.length <= 10^5
- 0 <= nums[i] <= 10^5
- 0 <= k <= 10^4
"""

def getAverages(nums, k):
    n = len(nums)
    res = [-1] * n
    if k == 0:
        return nums
    if 2*k+1 > n:
        return res
    window = sum(nums[:2*k+1])
    for i in range(k, n-k):
        res[i] = window // (2*k+1)
        if i + k + 1 < n:
            window += nums[i+k+1] - nums[i-k]
    return res

# Example usage:
# print(getAverages([7,4,3,9,1,8,5,2,6], 3))  # Output: [-1,-1,-1,5,4,4,-1,-1,-1]
