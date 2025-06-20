"""
290. Word Pattern
https://leetcode.com/problems/word-pattern/

Given a pattern and a string s, find if s follows the same pattern.

Constraints:
- 1 <= pattern.length <= 300
- s contains only lowercase English letters and spaces.
- 1 <= s.length <= 3000

Example 1:
Input: pattern = "abba", s = "dog cat cat dog"
Output: true

Example 2:
Input: pattern = "abba", s = "dog cat cat fish"
Output: false
"""
def wordPattern(pattern, s):
    words = s.split()
    if len(pattern) != len(words):
        return False
    p2w, w2p = {}, {}
    for p, w in zip(pattern, words):
        if (p in p2w and p2w[p] != w) or (w in w2p and w2p[w] != p):
            return False
        p2w[p] = w
        w2p[w] = p
    return True

# Example usage:
if __name__ == "__main__":
    print(wordPattern("abba", "dog cat cat dog"))   # Output: True
    print(wordPattern("abba", "dog cat cat fish"))  # Output: False
