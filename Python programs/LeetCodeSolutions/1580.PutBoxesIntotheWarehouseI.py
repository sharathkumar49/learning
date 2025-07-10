"""
LeetCode 1580. Put Boxes Into the Warehouse I

Given several boxes with different heights represented by an array boxes and a warehouse with n rooms represented by an array warehouse where warehouse[i] is the height of the ith room, return the maximum number of boxes you can put into the warehouse.

Example 1:
Input: boxes = [4,3,4,1], warehouse = [5,3,3,4,1]
Output: 3

Constraints:
- 1 <= boxes.length, warehouse.length <= 10^5
- 1 <= boxes[i], warehouse[i] <= 10^9
"""

def maxBoxesInWarehouse(boxes, warehouse):
    boxes.sort()
    n = len(warehouse)
    min_height = [0]*n
    min_height[0] = warehouse[0]
    for i in range(1, n):
        min_height[i] = min(min_height[i-1], warehouse[i])
    res = i = 0
    for h in reversed(min_height):
        if i < len(boxes) and boxes[i] <= h:
            res += 1
            i += 1
    return res

# Example usage:
# boxes = [4,3,4,1]
# warehouse = [5,3,3,4,1]
# print(maxBoxesInWarehouse(boxes, warehouse))  # Output: 3
