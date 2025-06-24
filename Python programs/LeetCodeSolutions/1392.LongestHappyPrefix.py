"""
LeetCode 1392. Longest Happy Prefix

A string is called a happy prefix if it is a non-empty prefix which is also a suffix (excluding itself). Given a string s, return the longest happy prefix of s. Return an empty string if no such prefix exists.

Constraints:
- 1 <= s.length <= 10^5
- s contains only lowercase English letters.

Example:
Input: s = "level"
Output: "l"
"""
def longestPrefix(s):
    n = len(s)
    lps = [0]*n
    length = 0
    i = 1
    while i < n:
        if s[i] == s[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length-1]
            else:
                lps[i] = 0
                i += 1
    return s[:lps[-1]]

# Example usage:
s = "level"
print(longestPrefix(s))  # Output: "l"
