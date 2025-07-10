"""
LeetCode 1558. Minimum Numbers of Function Calls to Make Target Array

Given an array nums, return the minimum number of function calls to make all elements in nums equal to zero. You can increment any element by 1 or double all elements.

Constraints:
- 1 <= nums.length <= 10^5
- 0 <= nums[i] <= 10^9

Example:
Input: nums = [1,5]
Output: 5
"""
def minOperations(nums):
    res = 0
    max_len = 0
    for x in nums:
        cnt = 0
        while x:
            if x % 2:
                res += 1
            x //= 2
            cnt += 1
        max_len = max(max_len, cnt-1 if cnt else 0)
    return res + max_len

# Example usage:
nums = [1,5]
print(minOperations(nums))  # Output: 5
