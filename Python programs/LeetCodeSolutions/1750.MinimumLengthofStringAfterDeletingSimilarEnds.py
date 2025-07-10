"""
LeetCode 1750. Minimum Length of String After Deleting Similar Ends

Given a string s, repeatedly delete the longest prefix and suffix that are the same, return the minimum length of s after all possible deletions.

Example 1:
Input: s = "ca"
Output: 2

Constraints:
- 1 <= s.length <= 10^5
- s consists only of lowercase English letters
"""

def minimumLength(s):
    l, r = 0, len(s) - 1
    while l < r and s[l] == s[r]:
        ch = s[l]
        while l <= r and s[l] == ch:
            l += 1
        while l <= r and s[r] == ch:
            r -= 1
    return r - l + 1

# Example usage:
# s = "ca"
# print(minimumLength(s))  # Output: 2
