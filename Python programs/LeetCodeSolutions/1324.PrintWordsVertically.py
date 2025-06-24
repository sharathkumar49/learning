"""
LeetCode 1324. Print Words Vertically

Given a string s, print the words vertically in the same order as they appear in s. Each column should be printed as a single string, with trailing spaces removed.

Constraints:
- 1 <= s.length <= 200
- s contains only uppercase English letters, lowercase English letters, and spaces.

Example:
Input: s = "HOW ARE YOU"
Output: ["HAY","ORO","WEU"]
"""
def printVertically(s):
    words = s.split()
    maxlen = max(len(w) for w in words)
    res = []
    for i in range(maxlen):
        col = ''.join(w[i] if i < len(w) else ' ' for w in words).rstrip()
        res.append(col)
    return res

# Example usage:
s = "HOW ARE YOU"
print(printVertically(s))  # Output: ['HAY', 'ORO', 'WEU']
