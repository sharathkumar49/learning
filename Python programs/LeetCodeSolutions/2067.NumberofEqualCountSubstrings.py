"""
LeetCode 2067. Number of Equal Count Substrings

Given a string s, return the number of substrings where each character appears the same number of times.

Example:
Input: s = "aaabcbbcc"
Output: 6

Constraints:
- 1 <= s.length <= 100
- s consists only of lowercase English letters.
"""

def equalCountSubstrings(s):
    n = len(s)
    res = 0
    for i in range(n):
        count = [0]*26
        for j in range(i, n):
            count[ord(s[j])-97] += 1
            vals = [x for x in count if x > 0]
            if len(set(vals)) == 1:
                res += 1
    return res

# Example usage:
# print(equalCountSubstrings("aaabcbbcc"))  # Output: 6
