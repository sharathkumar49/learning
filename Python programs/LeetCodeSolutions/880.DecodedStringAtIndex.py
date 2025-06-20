"""
880. Decoded String at Index

Given an encoded string s and an index k, return the k-th letter in the decoded string.

Example 1:
Input: s = "leet2code3", k = 10
Output: "o"

Example 2:
Input: s = "ha22", k = 5
Output: "h"

Constraints:
- 2 <= s.length <= 100
- s consists of lowercase English letters and digits 2-9.
- 1 <= k <= 10^9
- The decoded string is guaranteed to have less than 2^63 letters.
"""
def decodeAtIndex(s, k):
    size = 0
    for c in s:
        if c.isdigit():
            size *= int(c)
        else:
            size += 1
    for c in reversed(s):
        k %= size
        if k == 0 and c.isalpha():
            return c
        if c.isdigit():
            size //= int(c)
        else:
            size -= 1

# Example usage:
print(decodeAtIndex("leet2code3", 10))  # Output: "o"
print(decodeAtIndex("ha22", 5))         # Output: "h"
