"""
821. Shortest Distance to a Character

Given a string s and a character c, return an array of the shortest distance from each character in s to c.

Example 1:
Input: s = "loveleetcode", c = "e"
Output: [3,2,1,0,1,0,0,1,2,2,1,0]

Constraints:
- 1 <= s.length <= 10^4
- s[i] and c are lowercase English letters.
- c occurs at least once in s.
"""
def shortestToChar(s, c):
    n = len(s)
    res = [n] * n
    prev = -n
    for i in range(n):
        if s[i] == c:
            prev = i
        res[i] = i - prev
    prev = 2 * n
    for i in range(n-1, -1, -1):
        if s[i] == c:
            prev = i
        res[i] = min(res[i], abs(i - prev))
    return res

# Example usage:
print(shortestToChar("loveleetcode", "e"))  # Output: [3,2,1,0,1,0,0,1,2,2,1,0]
