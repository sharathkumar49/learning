"""
LeetCode 1371. Find the Longest Substring Containing Vowels in Even Counts

Given a string s, return the length of the longest substring where each vowel appears an even number of times.

Constraints:
- 1 <= s.length <= 5 * 10^5
- s consists of lowercase English letters only.

Example:
Input: s = "eleetminicoworoep"
Output: 13
"""
def findTheLongestSubstring(s):
    pos = {0: -1}
    mask = 0
    res = 0
    for i, c in enumerate(s):
        if c in 'aeiou':
            mask ^= 1 << 'aeiou'.index(c)
        if mask in pos:
            res = max(res, i - pos[mask])
        else:
            pos[mask] = i
    return res

# Example usage:
s = "eleetminicoworoep"
print(findTheLongestSubstring(s))  # Output: 13
