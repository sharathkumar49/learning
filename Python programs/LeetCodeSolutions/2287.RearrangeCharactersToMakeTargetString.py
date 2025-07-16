"""
LeetCode 2287. Rearrange Characters to Make Target String

Given s and target, return the maximum number of copies of target that can be formed.

Example:
Input: s = "ilovecodingonleetcode", target = "code"
Output: 2

Constraints:
- 1 <= s.length, target.length <= 100
"""

def rearrangeCharacters(s, target):
    from collections import Counter
    sc = Counter(s)
    tc = Counter(target)
    return min(sc[c]//tc[c] for c in tc)

# Example usage:
# print(rearrangeCharacters("ilovecodingonleetcode", "code"))  # Output: 2
