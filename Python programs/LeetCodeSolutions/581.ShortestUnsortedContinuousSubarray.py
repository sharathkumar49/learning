"""
581. Shortest Unsorted Continuous Subarray
Difficulty: Medium

Given an integer array nums, you need to find one continuous subarray that if you only sort this subarray in ascending order, then the whole array will be sorted in ascending order.
Return the shortest such subarray and output its length.

Example 1:
Input: nums = [2,6,4,8,10,9,15]
Output: 5
Explanation: You need to sort [6,4,8,10,9] in ascending order to make the whole array sorted.

Example 2:
Input: nums = [1,2,3,4]
Output: 0

Constraints:
1 <= nums.length <= 10^4
-10^5 <= nums[i] <= 10^5
"""

def findUnsortedSubarray(nums):
    n = len(nums)
    start, end = -1, -2
    min_num, max_num = nums[-1], nums[0]
    for i in range(1, n):
        max_num = max(max_num, nums[i])
        min_num = min(min_num, nums[n-1-i])
        if nums[i] < max_num:
            end = i
        if nums[n-1-i] > min_num:
            start = n-1-i
    return end - start + 1

# Example usage
if __name__ == "__main__":
    print(findUnsortedSubarray([2,6,4,8,10,9,15]))  # Output: 5
    print(findUnsortedSubarray([1,2,3,4]))          # Output: 0
