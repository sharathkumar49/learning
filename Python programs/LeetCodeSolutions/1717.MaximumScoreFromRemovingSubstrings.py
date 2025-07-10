"""
LeetCode 1717. Maximum Score From Removing Substrings

Given a string s and two integers x and y, you can remove substrings "ab" for x points and "ba" for y points. Return the maximum score you can get by removing these substrings.

Example 1:
Input: s = "cdbcbbaaabab", x = 4, y = 5
Output: 19

Constraints:
- 1 <= s.length <= 10^5
- 1 <= x, y <= 10^4
- s consists of 'a', 'b', and 'c'
"""

def maximumGain(s, x, y):
    def remove(s, a, b, val):
        stack = []
        score = 0
        for c in s:
            if stack and stack[-1] == a and c == b:
                stack.pop()
                score += val
            else:
                stack.append(c)
        return ''.join(stack), score
    if x > y:
        s, score1 = remove(s, 'a', 'b', x)
        _, score2 = remove(s, 'b', 'a', y)
    else:
        s, score1 = remove(s, 'b', 'a', y)
        _, score2 = remove(s, 'a', 'b', x)
    return score1 + score2

# Example usage:
# s = "cdbcbbaaabab"
# x = 4
# y = 5
# print(maximumGain(s, x, y))  # Output: 19
