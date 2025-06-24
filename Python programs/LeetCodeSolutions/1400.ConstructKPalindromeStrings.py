"""
LeetCode 1400. Construct K Palindrome Strings

Given a string s and an integer k, return true if you can use all the characters in s to construct k palindrome strings or false otherwise.

Constraints:
- 1 <= s.length <= 10^5
- 1 <= k <= 10^5
- s consists of lowercase English letters only.

Example:
Input: s = "annabelle", k = 2
Output: true
"""
def canConstruct(s, k):
    from collections import Counter
    odd = sum(v % 2 for v in Counter(s).values())
    return odd <= k <= len(s)

# Example usage:
s = "annabelle"
k = 2
print(canConstruct(s, k))  # Output: True
