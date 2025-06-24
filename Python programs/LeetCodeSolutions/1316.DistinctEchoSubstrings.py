"""
LeetCode 1316. Distinct Echo Substrings

Return the number of distinct echo substrings of s. An echo substring is a non-empty substring that can be written as the concatenation of some string with itself.

Constraints:
- 1 <= s.length <= 2000
- s consists of lowercase English letters only.

Example:
Input: s = "abcabcabc"
Output: 3
"""
def distinctEchoSubstrings(s):
    seen = set()
    n = len(s)
    for l in range(1, n//2+1):
        for i in range(n-2*l+1):
            if s[i:i+l] == s[i+l:i+2*l]:
                seen.add(s[i:i+2*l])
    return len(seen)

# Example usage:
s = "abcabcabc"
print(distinctEchoSubstrings(s))  # Output: 3
