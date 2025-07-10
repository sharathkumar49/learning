"""
LeetCode 2182. Construct String With Repeat Limit

Given a string s and an integer repeatLimit, construct the lexicographically largest string with no letter repeating more than repeatLimit times consecutively.

Example:
Input: s = "cczazcc", repeatLimit = 3
Output: "zzcccac"

Constraints:
- 1 <= s.length <= 10^5
- 1 <= repeatLimit <= s.length
- s consists of lowercase English letters.
"""

def repeatLimitedString(s, repeatLimit):
    from collections import Counter
    c = Counter(s)
    chars = sorted(c.keys(), reverse=True)
    res = []
    while chars:
        for i, ch in enumerate(chars):
            if not res or res[-1] != ch or res[-repeatLimit:] != [ch]*repeatLimit:
                res.append(ch)
                c[ch] -= 1
                if c[ch] == 0:
                    chars.pop(i)
                break
        else:
            break
    return ''.join(res)

# Example usage:
# print(repeatLimitedString("cczazcc", 3))  # Output: "zzcccac"
