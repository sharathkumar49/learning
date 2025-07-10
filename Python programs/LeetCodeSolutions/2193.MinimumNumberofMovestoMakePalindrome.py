"""
LeetCode 2193. Minimum Number of Moves to Make Palindrome

Given a string s, return the minimum number of adjacent swaps to make s a palindrome.

Example:
Input: s = "aabb"
Output: 2

Constraints:
- 1 <= s.length <= 2000
- s consists of lowercase English letters.
"""

def minMovesToMakePalindrome(s):
    s = list(s)
    res = 0
    while s:
        if s[0] == s[-1]:
            s.pop()
            s.pop(0)
        else:
            i = s.index(s[-1])
            if i == len(s)-1:
                res += len(s)//2
                s.pop()
            else:
                res += i
                s.pop(i)
                s.pop()
    return res

# Example usage:
# print(minMovesToMakePalindrome("aabb"))  # Output: 2
