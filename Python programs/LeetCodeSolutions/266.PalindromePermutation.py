"""
266. Palindrome Permutation
https://leetcode.com/problems/palindrome-permutation/

Given a string s, return true if a permutation of the string could form a palindrome.

Constraints:
- 1 <= s.length <= 5000
- s consists of only lowercase English letters.

Example 1:
Input: s = "code"
Output: false

Example 2:
Input: s = "aab"
Output: true

Example 3:
Input: s = "carerac"
Output: true
"""
def canPermutePalindrome(s):
    from collections import Counter
    count = Counter(s)
    odd = sum(v % 2 for v in count.values())
    return odd <= 1

# Example usage:
if __name__ == "__main__":
    print(canPermutePalindrome("code"))     # Output: False
    print(canPermutePalindrome("aab"))      # Output: True
    print(canPermutePalindrome("carerac"))  # Output: True
