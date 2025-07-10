"""
LeetCode 1528. Shuffle String

Given a string s and an integer array indices, return the shuffled string.

Constraints:
- s.length == indices.length == n
- 1 <= n <= 100
- s contains only lowercase English letters.
- 0 <= indices[i] < n

Example:
Input: s = "codeleet", indices = [4,5,6,7,0,2,1,3]
Output: "leetcode"
"""
def restoreString(s, indices):
    res = [''] * len(s)
    for i, c in enumerate(s):
        res[indices[i]] = c
    return ''.join(res)

# Example usage:
s = "codeleet"
indices = [4,5,6,7,0,2,1,3]
print(restoreString(s, indices))  # Output: "leetcode"
