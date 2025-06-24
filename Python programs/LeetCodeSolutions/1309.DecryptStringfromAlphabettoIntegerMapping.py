"""
LeetCode 1309. Decrypt String from Alphabet to Integer Mapping

Given a string s, return the string formed by mapping digits to letters as follows:
- '1' to '9' -> 'a' to 'i'
- '10#' to '26#' -> 'j' to 'z'

Constraints:
- 1 <= s.length <= 1000
- s consists of digits and the '#' character.

Example:
Input: s = "10#11#12"
Output: "jkab"
"""
def freqAlphabets(s):
    res = ''
    i = 0
    while i < len(s):
        if i+2 < len(s) and s[i+2] == '#':
            res += chr(int(s[i:i+2]) + 96)
            i += 3
        else:
            res += chr(int(s[i]) + 96)
            i += 1
    return res

# Example usage:
s = "10#11#12"
print(freqAlphabets(s))  # Output: "jkab"
