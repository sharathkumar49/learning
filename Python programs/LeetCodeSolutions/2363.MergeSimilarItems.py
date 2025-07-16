"""
LeetCode 2363. Merge Similar Items

Given items1 and items2, return the merged items sorted by value.

Example:
Input: items1 = [[1,1],[4,5],[3,8]], items2 = [[3,1],[1,5]]
Output: [[1,6],[3,9],[4,5]]

Constraints:
- 1 <= items1.length, items2.length <= 1000
"""

def mergeSimilarItems(items1, items2):
    from collections import Counter
    c = Counter()
    for v, w in items1+items2:
        c[v] += w
    return sorted([[v, c[v]] for v in c])

# Example usage:
# print(mergeSimilarItems([[1,1],[4,5],[3,8]], [[3,1],[1,5]]))  # Output: [[1,6],[3,9],[4,5]]
