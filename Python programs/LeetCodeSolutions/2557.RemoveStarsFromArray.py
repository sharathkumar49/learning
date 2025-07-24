"""
LeetCode 2557. Remove Stars From Array

Given an array, remove stars and the closest non-star element to the left for each star.

Constraints:
- 1 <= nums.length <= 10^5
"""

def removeStars(nums):
    stack = []
    for x in nums:
        if x == '*':
            if stack:
                stack.pop()
        else:
            stack.append(x)
    return stack
# Example usage:
# print(removeStars([1,'*',2,'*',3]))  # Output: [3]
