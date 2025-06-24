"""
LeetCode 1332. Remove Palindromic Subsequences

Given a string s consisting only of 'a' and 'b', return the minimum number of steps to make the string empty by removing palindromic subsequences.

Constraints:
- 1 <= s.length <= 1000
- s consists only of 'a' and 'b'.

Example:
Input: s = "ababa"
Output: 1
"""
def removePalindromeSub(s):
    return 1 if s == s[::-1] else 2

# Example usage:
s = "ababa"
print(removePalindromeSub(s))  # Output: 1
