"""
LeetCode 2626. Array Reduce Transformation

Implement a reduce function for a list.

Constraints:
- 0 <= arr.length <= 10^5
"""

def reduce(arr, fn, init):
    res = init
    for x in arr:
        res = fn(res, x)
    return res
# Example usage:
# print(reduce([1,2,3,4], lambda acc, cur: acc + cur, 0))  # Output: 10
