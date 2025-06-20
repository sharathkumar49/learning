"""
647. Palindromic Substrings
Difficulty: Medium

Given a string s, return the number of palindromic substrings in it.

Example 1:
Input: s = "abc"
Output: 3

Example 2:
Input: s = "aaa"
Output: 6

Constraints:
1 <= s.length <= 1000
s consists of lowercase English letters.
"""

def countSubstrings(s):
    n = len(s)
    res = 0
    for i in range(n):
        for j in range(2):
            l, r = i, i+j
            while l >= 0 and r < n and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1
    return res

# Example usage
if __name__ == "__main__":
    print(countSubstrings("abc"))  # Output: 3
    print(countSubstrings("aaa"))  # Output: 6
