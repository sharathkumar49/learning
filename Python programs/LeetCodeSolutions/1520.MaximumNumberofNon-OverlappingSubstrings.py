"""
LeetCode 1520. Maximum Number of Non-Overlapping Substrings

Given a string s, return the maximum number of non-overlapping substrings of s such that each substring is minimal and contains all occurrences of every character it contains.

Constraints:
- 1 <= s.length <= 10^5
- s consists of lowercase English letters.

Example:
Input: s = "adefaddaccc"
Output: ["e","f","ccc"]
"""
def maxNumOfSubstrings(s):
    first = {c: i for i, c in enumerate(s) if c not in first}
    last = {c: i for i, c in enumerate(s)}
    res = []
    intervals = []
    for c in set(s):
        l, r = first[c], last[c]
        i = l
        while i <= r:
            if first[s[i]] < l or last[s[i]] > r:
                l = min(l, first[s[i]])
                r = max(r, last[s[i]])
                i = l
            else:
                i += 1
        intervals.append((l, r))
    intervals.sort(key=lambda x: x[1])
    end = -1
    for l, r in intervals:
        if l > end:
            res.append(s[l:r+1])
            end = r
    return res

# Example usage:
s = "adefaddaccc"
print(maxNumOfSubstrings(s))  # Output: ['e', 'f', 'ccc']
