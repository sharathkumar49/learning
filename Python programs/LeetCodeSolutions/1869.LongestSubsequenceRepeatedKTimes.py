"""
LeetCode 1869. Longest Subsequence Repeated k Times

Given a string s and an integer k, return the longest subsequence repeated k times in s. If there are multiple, return the lexicographically largest one.

Example:
Input: s = "letsleetcode", k = 2
Output: "let"

Constraints:
- 2 <= s.length <= 2000
- 2 <= k <= 2000
- s consists of lowercase English letters.
"""

def longestSubsequenceRepeatedK(s, k):
    from collections import Counter
    from itertools import product
    cnt = Counter(s)
    chars = [c for c in cnt if cnt[c] >= k]
    chars.sort(reverse=True)
    def is_valid(sub):
        i = 0
        for c in s:
            if c == sub[i]:
                i += 1
                if i == len(sub):
                    i = 0
                    k_ = k - 1
                    for c2 in s[s.index(c)+1:]:
                        if c2 == sub[i]:
                            i += 1
                            if i == len(sub):
                                i = 0
                                k_ -= 1
                                if k_ == 0:
                                    return True
                    return False
        return False
    for l in range(len(s)//k, 0, -1):
        for cand in product(chars, repeat=l):
            cand_str = ''.join(cand)
            if is_valid(cand_str):
                return cand_str
    return ""

# Example usage:
# print(longestSubsequenceRepeatedK("letsleetcode", 2))  # Output: "let"
