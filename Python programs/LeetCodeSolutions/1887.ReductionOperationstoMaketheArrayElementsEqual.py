"""
LeetCode 1887. Reduction Operations to Make the Array Elements Equal

Given an integer array nums, return the minimum number of operations to make all elements equal. In one operation, you can decrease the largest element to the next largest element.

Example:
Input: nums = [5,1,3]
Output: 3

Constraints:
- 1 <= nums.length <= 5 * 10^4
- 1 <= nums[i] <= 5 * 10^5
"""

def reductionOperations(nums):
    nums.sort()
    res = cnt = 0
    for i in range(1, len(nums)):
        if nums[i] != nums[i-1]:
            cnt += 1
        res += cnt
    return res

# Example usage:
# print(reductionOperations([5,1,3]))  # Output: 3
