"""
1003. Check If Word Is Valid After Substitutions

Given a string s, determine if it is valid. A string s is valid if, starting with an empty string t = "", you can transform t into s after performing the following operation any number of times:
- Insert string "abc" into any position in t. More formally, t becomes t[0:pos] + "abc" + t[pos:]

Return true if s is a valid string, otherwise, return false.

Example 1:
Input: s = "aabcbc"
Output: true
Explanation:
"" -> "abc" -> "aabcbc"

Example 2:
Input: s = "abcabcababcc"
Output: true
Explanation:
"" -> "abc" -> "abcabc" -> "abcabcabc" -> "abcabcababcc"

Example 3:
Input: s = "abccba"
Output: false

Constraints:
- 1 <= s.length <= 2 * 10^4
- s consists of letters 'a', 'b', and 'c'
"""
def isValid(s: str) -> bool:
    stack = []
    for ch in s:
        stack.append(ch)
        if len(stack) >= 3 and stack[-3:] == ['a', 'b', 'c']:
            stack[-3:] = []
    return not stack

# Example usage
if __name__ == "__main__":
    print(isValid("aabcbc"))           # Output: True
    print(isValid("abcabcababcc"))     # Output: True
    print(isValid("abccba"))           # Output: False
