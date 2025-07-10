"""
LeetCode 1781. Sum of Beauty of All Substrings

Given a string s, return the sum of beauty of all substrings. The beauty of a string is the difference between the maximum and minimum frequency of characters in it.

Example 1:
Input: s = "aabcb"
Output: 5

Constraints:
- 1 <= s.length <= 500
- s consists of lowercase English letters
"""

def beautySum(s):
    res = 0
    n = len(s)
    for i in range(n):
        count = [0]*26
        for j in range(i, n):
            count[ord(s[j])-97] += 1
            mx = max([c for c in count if c])
            mn = min([c for c in count if c])
            res += mx - mn
    return res

# Example usage:
# s = "aabcb"
# print(beautySum(s))  # Output: 5
