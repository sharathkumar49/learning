"""
567. Permutation in String
Difficulty: Medium

Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.
In other words, return true if one of s1's permutations is the substring of s2.

Example 1:
Input: s1 = "ab", s2 = "eidbaooo"
Output: true

Example 2:
Input: s1 = "ab", s2 = "eidboaoo"
Output: false

Constraints:
1 <= s1.length, s2.length <= 10^4
s1 and s2 consist of lowercase English letters.
"""

def checkInclusion(s1: str, s2: str) -> bool:
    from collections import Counter
    n, m = len(s1), len(s2)
    if n > m:
        return False
    s1_count = Counter(s1)
    window = Counter(s2[:n])
    if window == s1_count:
        return True
    for i in range(n, m):
        window[s2[i]] += 1
        window[s2[i-n]] -= 1
        if window[s2[i-n]] == 0:
            del window[s2[i-n]]
        if window == s1_count:
            return True
    return False

# Example usage
if __name__ == "__main__":
    print(checkInclusion("ab", "eidbaooo"))  # Output: True
    print(checkInclusion("ab", "eidboaoo")) # Output: False
