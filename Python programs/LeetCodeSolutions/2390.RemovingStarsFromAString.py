"""
LeetCode 2390. Removing Stars From a String

Given a string s, remove stars and the closest non-star character to the left for each star.

Constraints:
- 1 <= s.length <= 10^5
"""

def removeStars(s):
    stack = []
    for c in s:
        if c == '*':
            if stack:
                stack.pop()
        else:
            stack.append(c)
    return ''.join(stack)

# Example usage:
# print(removeStars("leet**cod*e"))  # Output: "lecoe"
