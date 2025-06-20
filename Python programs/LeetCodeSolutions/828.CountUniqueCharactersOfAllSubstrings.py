"""
828. Count Unique Characters of All Substrings of a Given String

Given a string s, return the sum of count of unique characters of all substrings of s.

Example 1:
Input: s = "ABC"
Output: 10

Example 2:
Input: s = "ABA"
Output: 8

Constraints:
- 1 <= s.length <= 10^4
- s consists of uppercase English letters only.
"""
def uniqueLetterString(s):
    index = {c: [-1, -1] for c in set(s)}
    res = 0
    for i, c in enumerate(s):
        k, j = index[c]
        res += (i - j) * (j - k)
        index[c] = [j, i]
    n = len(s)
    for c in index:
        k, j = index[c]
        res += (n - j) * (j - k)
    return res

# Example usage:
print(uniqueLetterString("ABC"))  # Output: 10
print(uniqueLetterString("ABA"))  # Output: 8
