"""
LeetCode 2486. Append Characters to String to Make Subsequence

Given two strings, return the minimum number of characters to append to make s a subsequence of t.

Constraints:
- 1 <= s.length, t.length <= 10^5
"""

def appendCharacters(s, t):
    i = 0
    for c in t:
        if i < len(s) and s[i] == c:
            i += 1
    return len(s)-i

# Example usage:
# print(appendCharacters("coaching","coding"))  # Output: 4
