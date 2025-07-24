"""
LeetCode 2631. Group By

Implement a group by function for a list.

Constraints:
- 1 <= arr.length <= 10^5
"""

def groupBy(arr, fn):
    from collections import defaultdict
    d = defaultdict(list)
    for x in arr:
        d[fn(x)].append(x)
    return dict(d)
# Example usage:
# print(groupBy([1,2,3,4], lambda x: x%2))  # Output: {1: [1, 3], 0: [2, 4]}
