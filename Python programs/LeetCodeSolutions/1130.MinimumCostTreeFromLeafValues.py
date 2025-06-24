"""
1130. Minimum Cost Tree From Leaf Values

Given an array arr of positive integers, consider all binary trees such that each node has either 0 or 2 children, and each leaf node's value is from arr. The value of each non-leaf node is equal to the product of the largest leaf values in its left and right subtree. Return the minimum possible sum of the values of each non-leaf node.

Constraints:
- 2 <= arr.length <= 40
- 1 <= arr[i] <= 15

Example:
Input: arr = [6,2,4]
Output: 32
"""
from typing import List

def mctFromLeafValues(arr: List[int]) -> int:
    res = 0
    stack = [float('inf')]
    for a in arr:
        while stack[-1] <= a:
            mid = stack.pop()
            res += mid * min(stack[-1], a)
        stack.append(a)
    while len(stack) > 2:
        res += stack.pop() * stack[-1]
    return res

# Example usage:
arr = [6,2,4]
print(mctFromLeafValues(arr))  # Output: 32
