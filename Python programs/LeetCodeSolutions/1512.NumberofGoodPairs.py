"""
LeetCode 1512. Number of Good Pairs

Given an array of integers nums, return the number of good pairs. A pair (i, j) is good if nums[i] == nums[j] and i < j.

Constraints:
- 1 <= nums.length <= 100
- 1 <= nums[i] <= 100

Example:
Input: nums = [1,2,3,1,1,3]
Output: 4
"""
def numIdenticalPairs(nums):
    from collections import Counter
    count = Counter(nums)
    return sum(v*(v-1)//2 for v in count.values())

# Example usage:
nums = [1,2,3,1,1,3]
print(numIdenticalPairs(nums))  # Output: 4
