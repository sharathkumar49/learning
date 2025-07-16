"""
LeetCode 2455. Average Value of Even Numbers That Are Divisible by Three

Given an array, return the average value of even numbers divisible by three.

Constraints:
- 1 <= nums.length <= 1000
"""

def averageValue(nums):
    vals = [x for x in nums if x%6==0]
    return sum(vals)//len(vals) if vals else 0

# Example usage:
# print(averageValue([1,3,6,10,12,15]))  # Output: 9
