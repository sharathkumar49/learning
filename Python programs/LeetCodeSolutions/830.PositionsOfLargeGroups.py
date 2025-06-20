"""
830. Positions of Large Groups

In a string s of lowercase letters, a large group is a group of 3 or more consecutive characters. Return the start and end positions of every large group.

Example 1:
Input: s = "abbxxxxzzy"
Output: [[3,6]]

Example 2:
Input: s = "abc"
Output: []

Constraints:
- 1 <= s.length <= 1000
- s consists of lowercase English letters.
"""
def largeGroupPositions(s):
    res = []
    i = 0
    n = len(s)
    while i < n:
        j = i
        while j < n and s[j] == s[i]:
            j += 1
        if j - i >= 3:
            res.append([i, j-1])
        i = j
    return res

# Example usage:
print(largeGroupPositions("abbxxxxzzy"))  # Output: [[3,6]]
print(largeGroupPositions("abc"))         # Output: []
