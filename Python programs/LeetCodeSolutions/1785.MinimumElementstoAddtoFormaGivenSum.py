"""
LeetCode 1785. Minimum Elements to Add to Form a Given Sum

Given an array nums, an integer limit, and an integer goal, return the minimum number of elements to add to make the sum of nums equal to goal, where each added element is in [-limit, limit].

Example 1:
Input: nums = [1,-1,1], limit = 3, goal = -4
Output: 2

Constraints:
- 1 <= nums.length <= 10^5
- 1 <= limit <= 10^6
- -10^9 <= goal <= 10^9
"""

def minElements(nums, limit, goal):
    diff = abs(goal - sum(nums))
    return (diff + limit - 1) // limit

# Example usage:
# nums = [1,-1,1]
# limit = 3
# goal = -4
# print(minElements(nums, limit, goal))  # Output: 2
