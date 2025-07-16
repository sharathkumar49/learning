"""
LeetCode 2272. Substring With Largest Variance

Given a string s, return the largest variance among all substrings.

Example:
Input: s = "aababbb"
Output: 3

Constraints:
- 1 <= s.length <= 10^4
- s consists of lowercase English letters
"""

def largestVariance(s):
    res = 0
    for a in set(s):
        for b in set(s):
            if a == b:
                continue
            diff = 0
            has_b = False
            max_diff = 0
            for c in s:
                if c == a:
                    diff += 1
                elif c == b:
                    diff -= 1
                    has_b = True
                if has_b:
                    max_diff = max(max_diff, diff)
                if diff < 0:
                    diff = 0
                    has_b = False
            res = max(res, max_diff)
    return res

# Example usage:
# print(largestVariance("aababbb"))  # Output: 3
