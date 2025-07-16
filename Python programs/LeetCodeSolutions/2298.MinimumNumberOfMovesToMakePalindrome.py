"""
LeetCode 2298. Minimum Number of Moves to Make Palindrome

Given s, return the minimum number of moves to make s a palindrome.

Example:
Input: s = "aabb"
Output: 2

Constraints:
- 1 <= s.length <= 2000
"""

def minMovesToMakePalindrome(s):
    s = list(s)
    res = 0
    while s:
        i = s.index(s[-1]) if s.count(s[-1]) > 1 else 0
        res += len(s)-i-1
        s.pop(i)
        s.pop()
    return res

# Example usage:
# print(minMovesToMakePalindrome("aabb"))  # Output: 2
