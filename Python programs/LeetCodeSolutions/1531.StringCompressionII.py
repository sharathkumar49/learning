"""
LeetCode 1531. String Compression II

Given a string s and an integer k, return the length of the shortest string that can be achieved by deleting at most k characters and compressing the string as in run-length encoding.

Constraints:
- 1 <= s.length <= 100
- 0 <= k <= s.length

Example:
Input: s = "aaabcccd", k = 2
Output: 4
"""
def getLengthOfOptimalCompression(s, k):
    from functools import lru_cache
    @lru_cache(None)
    def dp(i, k, last, last_count):
        if k < 0:
            return float('inf')
        if i == len(s):
            return 0
        # delete s[i]
        res = dp(i+1, k-1, last, last_count)
        # keep s[i]
        if s[i] == last:
            add = 1 if last_count in [1,9,99] else 0
            res = min(res, add + dp(i+1, k, last, last_count+1))
        else:
            res = min(res, 1 + dp(i+1, k, s[i], 1))
        return res
    return dp(0, k, '', 0)

# Example usage:
s = "aaabcccd"
k = 2
print(getLengthOfOptimalCompression(s, k))  # Output: 4
