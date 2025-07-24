"""
LeetCode 2734. Lexicographically Smallest String After Substring Operation

Given s, return the lexicographically smallest string after one substring operation.

Constraints:
- 1 <= s.length <= 100
"""

def smallestString(s):
    s = list(s)
    for i in range(len(s)):
        if s[i] != 'a':
            while i < len(s) and s[i] != 'a':
                s[i] = chr(ord(s[i])-1)
                i += 1
            break
    else:
        s[-1] = 'z'
    return ''.join(s)
# Example usage:
# print(smallestString("cbabc"))  # Output: "baabc"
