"""
LeetCode 1758. Minimum Changes To Make Alternating Binary String

Given a binary string s, return the minimum number of changes to make the string alternating.

Example 1:
Input: s = "0100"
Output: 1

Constraints:
- 1 <= s.length <= 10^4
- s[i] is '0' or '1'
"""

def minOperations(s):
    alt1 = sum(int(c) != i%2 for i, c in enumerate(s))
    alt2 = sum(int(c) != (i+1)%2 for i, c in enumerate(s))
    return min(alt1, alt2)

# Example usage:
# s = "0100"
# print(minOperations(s))  # Output: 1
