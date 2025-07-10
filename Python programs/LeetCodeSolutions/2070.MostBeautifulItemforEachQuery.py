"""
LeetCode 2070. Most Beautiful Item for Each Query

Given items with beauty and price, and a list of queries, return the maximum beauty for each query price.

Example:
Input: items = [[1,2],[3,2],[2,4],[5,6]], queries = [1,2,3,4,5,6]
Output: [0,2,2,4,6,6]

Constraints:
- 1 <= items.length, queries.length <= 10^5
- 1 <= price, beauty <= 10^9
"""

def maximumBeauty(items, queries):
    items.sort()
    arr = []
    max_beauty = 0
    for price, beauty in items:
        max_beauty = max(max_beauty, beauty)
        arr.append((price, max_beauty))
    import bisect
    res = []
    for q in queries:
        idx = bisect.bisect_right(arr, (q, float('inf'))) - 1
        res.append(arr[idx][1] if idx >= 0 else 0)
    return res

# Example usage:
# print(maximumBeauty([[1,2],[3,2],[2,4],[5,6]], [1,2,3,4,5,6]))  # Output: [0,2,2,4,6,6]
