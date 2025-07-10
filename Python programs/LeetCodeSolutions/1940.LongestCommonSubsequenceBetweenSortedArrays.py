"""
LeetCode 1940. Longest Common Subsequence Between Sorted Arrays

Given a list of sorted arrays, return the longest common subsequence present in all arrays.

Example:
Input: arrays = [[1,2,3,4,5],[1,2,5,7,9],[1,3,4,5,8,9]]
Output: [1,5]

Constraints:
- 2 <= arrays.length <= 100
- 1 <= arrays[i].length <= 100
- 1 <= arrays[i][j] <= 100
"""

def longestCommonSubsequence(arrays):
    from collections import Counter
    count = Counter()
    for arr in arrays:
        count.update(set(arr))
    n = len(arrays)
    return sorted([x for x in count if count[x] == n])

# Example usage:
# print(longestCommonSubsequence([[1,2,3,4,5],[1,2,5,7,9],[1,3,4,5,8,9]]))  # Output: [1,5]
