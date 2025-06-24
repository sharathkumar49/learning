"""
LeetCode 1320. Minimum Distance to Type a Word Using Two Fingers

Given a word, return the minimum distance to type it using two fingers on a keyboard with 26 letters in a 6x5 grid.

Constraints:
- 2 <= word.length <= 300
- word consists of uppercase English letters.

Example:
Input: word = "CAKE"
Output: 3
"""
def minimumDistance(word):
    from functools import lru_cache
    def pos(c):
        i = ord(c) - ord('A')
        return divmod(i, 6)
    n = len(word)
    @lru_cache(None)
    def dp(i, f1, f2):
        if i == n:
            return 0
        p = pos(word[i])
        res = float('inf')
        if f1 is None:
            res = min(res, dp(i+1, p, f2))
        else:
            res = min(res, dp(i+1, p, f2) + abs(f1[0]-p[0]) + abs(f1[1]-p[1]))
        if f2 is None:
            res = min(res, dp(i+1, f1, p))
        else:
            res = min(res, dp(i+1, f1, p) + abs(f2[0]-p[0]) + abs(f2[1]-p[1]))
        return res
    return dp(0, None, None)

# Example usage:
word = "CAKE"
print(minimumDistance(word))  # Output: 3
