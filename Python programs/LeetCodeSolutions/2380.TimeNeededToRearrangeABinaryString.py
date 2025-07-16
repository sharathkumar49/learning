"""
LeetCode 2380. Time Needed to Rearrange a Binary String

Given a binary string, return the time needed to rearrange so that all '0's are before '1's.

Constraints:
- 1 <= s.length <= 10^5
"""

def secondsToRemoveOccurrences(s):
    s = list(s)
    res = 0
    while True:
        changed = False
        i = 0
        while i < len(s)-1:
            if s[i] == '1' and s[i+1] == '0':
                s[i], s[i+1] = s[i+1], s[i]
                changed = True
                i += 1
            i += 1
        if not changed:
            break
        res += 1
    return res

# Example usage:
# print(secondsToRemoveOccurrences("0110101"))  # Output: 4
