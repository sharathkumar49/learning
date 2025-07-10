"""
LeetCode 1769. Minimum Number of Operations to Move All Balls to Each Box

Given a binary string boxes, return an array of the minimum number of operations to move all balls to each box.

Example 1:
Input: boxes = "110"
Output: [1,1,3]

Constraints:
- 1 <= boxes.length <= 2000
- boxes[i] is '0' or '1'
"""

def minOperations(boxes):
    n = len(boxes)
    res = [0]*n
    left = right = 0
    ops = 0
    for i in range(n):
        res[i] += ops
        left += int(boxes[i])
        ops += left
    left = ops = 0
    for i in range(n-1, -1, -1):
        res[i] += ops
        left += int(boxes[i])
        ops += left
    return res

# Example usage:
# boxes = "110"
# print(minOperations(boxes))  # Output: [1,1,3]
