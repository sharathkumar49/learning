"""
LeetCode 2197. Replace Non-Coprime Numbers in Array

Given an array nums, replace adjacent non-coprime numbers with their LCM until no more replacements can be made. Return the resulting array.

Example:
Input: nums = [6,4,3,2,7,6,2]
Output: [12,7,6]

Constraints:
- 1 <= nums.length <= 10^5
- 1 <= nums[i] <= 10^8
"""

def replaceNonCoprimes(nums):
    from math import gcd
    stack = []
    for x in nums:
        while stack and gcd(stack[-1], x) > 1:
            x = x * stack.pop() // gcd(stack[-1], x)
        stack.append(x)
    return stack

# Example usage:
# print(replaceNonCoprimes([6,4,3,2,7,6,2]))  # Output: [12,7,6]
