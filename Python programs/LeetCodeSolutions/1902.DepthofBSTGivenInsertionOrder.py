"""
LeetCode 1902. Depth of BST Given Insertion Order

Given an array order, return the depth of the BST formed by inserting the elements in order.

Example:
Input: order = [2,1,4,3]
Output: 3

Constraints:
- 1 <= order.length <= 10^5
- 1 <= order[i] <= 10^5
"""

def bstDepth(order):
    import bisect
    arr = []
    depth = {}
    for x in order:
        i = bisect.bisect_left(arr, x)
        left = arr[i-1] if i > 0 else None
        right = arr[i] if i < len(arr) else None
        d = 1 + max(depth.get(left, 0), depth.get(right, 0))
        depth[x] = d
        arr.insert(i, x)
    return max(depth.values())

# Example usage:
# print(bstDepth([2,1,4,3]))  # Output: 3
