"""
LeetCode 2301. Match Substring After Replacement

Given s, sub, and mappings, return true if sub can be matched in s after replacements.

Example:
Input: s = "foolbar", sub = "foobar", mappings = [["o","a"]]
Output: True

Constraints:
- 1 <= s.length, sub.length <= 10^5
- 1 <= mappings.length <= 10^5
"""

def matchReplacement(s, sub, mappings):
    from collections import defaultdict
    mp = defaultdict(set)
    for a, b in mappings:
        mp[a].add(b)
    for i in range(len(s)-len(sub)+1):
        for j in range(len(sub)):
            if s[i+j] != sub[j] and sub[j] not in mp[s[i+j]]:
                break
        else:
            return True
    return False

# Example usage:
# print(matchReplacement("foolbar", "foobar", [["o","a"]]))  # Output: True
