"""
LeetCode 1593. Split a String Into the Max Number of Unique Substrings

Given a string s, return the maximum number of unique substrings that the string can be split into.

Example 1:
Input: s = "ababccc"
Output: 5

Constraints:
- 1 <= s.length <= 16
- s consists of only lowercase English letters.
"""

def maxUniqueSplit(s):
    def dfs(start, seen):
        if start == len(s):
            return len(seen)
        res = 0
        for end in range(start+1, len(s)+1):
            sub = s[start:end]
            if sub not in seen:
                seen.add(sub)
                res = max(res, dfs(end, seen))
                seen.remove(sub)
        return res
    return dfs(0, set())

# Example usage:
# s = "ababccc"
# print(maxUniqueSplit(s))  # Output: 5
