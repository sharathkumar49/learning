"""
LeetCode 1653. Minimum Deletions to Make String Balanced

Given a string s consisting of 'a' and 'b', return the minimum number of deletions needed to make s balanced (all 'a's before all 'b's).

Example 1:
Input: s = "aababbab"
Output: 2

Constraints:
- 1 <= s.length <= 10^5
- s consists of only 'a' and 'b'.
"""

def minimumDeletions(s):
    res = 0
    b = 0
    for c in s:
        if c == 'b':
            b += 1
        else:
            res = min(res+1, b)
    return res

# Example usage:
s = "aababbab"
print("minimum deletions required: ", minimumDeletions(s))  # Output: 2
