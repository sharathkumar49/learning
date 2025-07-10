"""
LeetCode 1564. Put Boxes Into the Warehouse I

Given an array boxes and an array warehouse, return the maximum number of boxes you can put into the warehouse.

Constraints:
- 1 <= boxes.length, warehouse.length <= 10^5
- 1 <= boxes[i], warehouse[i] <= 10^9

Example:
Input: boxes = [4,3,4,1], warehouse = [5,3,3,4]
Output: 3
"""
def maxBoxesInWarehouse(boxes, warehouse):
    boxes.sort()
    n = len(warehouse)
    for i in range(1, n):
        warehouse[i] = min(warehouse[i], warehouse[i-1])
    res = i = 0
    for w in reversed(warehouse):
        if i < len(boxes) and boxes[i] <= w:
            res += 1
            i += 1
    return res

# Example usage:
boxes = [4,3,4,1]
warehouse = [5,3,3,4]
print(maxBoxesInWarehouse(boxes, warehouse))  # Output: 3
