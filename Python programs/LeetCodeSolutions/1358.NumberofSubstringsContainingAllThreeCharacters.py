"""
LeetCode 1358. Number of Substrings Containing All Three Characters

Given a string s consisting only of 'a', 'b', and 'c', return the number of substrings containing at least one occurrence of each character.

Constraints:
- 3 <= s.length <= 5 * 10^4
- s consists only of 'a', 'b', and 'c'.

Example:
Input: s = "abcabc"
Output: 10
"""
def numberOfSubstrings(s):
    last = [-1, -1, -1]
    res = 0
    for i, c in enumerate(s):
        last[ord(c)-ord('a')] = i
        res += 1 + min(last)
    return res

# Example usage:
s = "abcabc"
print(numberOfSubstrings(s))  # Output: 10
