"""
291. Word Pattern II
https://leetcode.com/problems/word-pattern-ii/

Given a pattern and a string s, return true if s matches the pattern.
Each character in the pattern is mapped to a non-empty substring in s. The mapping must be a bijection.

Constraints:
- 1 <= pattern.length, s.length <= 20
- pattern and s consist of only lowercase English letters.

Example 1:
Input: pattern = "abab", s = "redblueredblue"
Output: true

Example 2:
Input: pattern = "aaaa", s = "asdasdasdasd"
Output: true

Example 3:
Input: pattern = "aabb", s = "xyzabcxzyabc"
Output: false
"""
def wordPatternMatch(pattern, s):
    def backtrack(p_idx, s_idx, p2s, s2p):
        if p_idx == len(pattern) and s_idx == len(s):
            return True
        if p_idx == len(pattern) or s_idx == len(s):
            return False
        p = pattern[p_idx]
        for end in range(s_idx+1, len(s)+1):
            sub = s[s_idx:end]
            if p not in p2s and sub not in s2p:
                p2s[p] = sub
                s2p[sub] = p
                if backtrack(p_idx+1, end, p2s, s2p):
                    return True
                del p2s[p]
                del s2p[sub]
            elif p in p2s and p2s[p] == sub:
                if backtrack(p_idx+1, end, p2s, s2p):
                    return True
        return False
    return backtrack(0, 0, {}, {})

# Example usage:
if __name__ == "__main__":
    print(wordPatternMatch("abab", "redblueredblue"))  # Output: True
    print(wordPatternMatch("aaaa", "asdasdasdasd"))    # Output: True
    print(wordPatternMatch("aabb", "xyzabcxzyabc"))    # Output: False
