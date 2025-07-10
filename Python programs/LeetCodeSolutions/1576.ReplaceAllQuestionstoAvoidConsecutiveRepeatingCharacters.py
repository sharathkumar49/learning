"""
LeetCode 1576. Replace All ?'s to Avoid Consecutive Repeating Characters

Given a string s containing only lowercase English letters and '?', replace every '?' with a lowercase letter so that no two adjacent characters are the same. Return any possible result.

Constraints:
- 1 <= s.length <= 100
- s consists of lowercase English letters and '?'.

Example:
Input: s = "?zs"
Output: "azs"
"""
def modifyString(s):
    s = list(s)
    for i in range(len(s)):
        if s[i] == '?':
            for c in 'abc':
                if (i == 0 or s[i-1] != c) and (i == len(s)-1 or s[i+1] != c):
                    s[i] = c
                    break
    return ''.join(s)

# Example usage:
s = "?zs"
print(modifyString(s))  # Output: "azs"
