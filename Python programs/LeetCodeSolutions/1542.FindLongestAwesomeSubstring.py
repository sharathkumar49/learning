"""
LeetCode 1542. Find Longest Awesome Substring

Given a string s, return the length of the longest awesome substring of s. An awesome substring is a substring that can be rearranged into a palindrome.

Constraints:
- 1 <= s.length <= 10^5
- s consists of digits.

Example:
Input: s = "3242415"
Output: 5
"""
def longestAwesome(s):
    pos = {0: -1}
    mask = 0
    res = 0
    for i, c in enumerate(s):
        mask ^= 1 << int(c)
        if mask in pos:
            res = max(res, i - pos[mask])
        for j in range(10):
            m2 = mask ^ (1 << j)
            if m2 in pos:
                res = max(res, i - pos[m2])
        if mask not in pos:
            pos[mask] = i
    return res

# Example usage:
s = "3242415"
print(longestAwesome(s))  # Output: 5
