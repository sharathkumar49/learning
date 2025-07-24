"""
LeetCode 2696. Minimum String Length After Removing Substrings

Given s, return the minimum length after removing substrings.

Constraints:
- 1 <= s.length <= 100
"""

def minLength(s):
    stack = []
    for c in s:
        if stack and ((stack[-1], c) in [('A','B'),('B','A'),('C','D'),('D','C')]):
            stack.pop()
        else:
            stack.append(c)
    return len(stack)
# Example usage:
# print(minLength("ABFCACDB"))  # Output: 2
