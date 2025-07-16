"""
LeetCode 2222. Number of Ways to Select Buildings

Given a string s, return the number of ways to select three buildings such that no two adjacent buildings are selected and the selected buildings are of different types.

Example:
Input: s = "001101"
Output: 6

Constraints:
- 3 <= s.length <= 10^5
- s[i] is '0' or '1'
"""

def numberOfWays(s):
    n = len(s)
    count0 = [0]*n
    count1 = [0]*n
    count0[0] = int(s[0] == '0')
    count1[0] = int(s[0] == '1')
    for i in range(1, n):
        count0[i] = count0[i-1] + (s[i] == '0')
        count1[i] = count1[i-1] + (s[i] == '1')
    res = 0
    for i in range(1, n-1):
        if s[i] == '0':
            res += count1[i-1] * (count1[n-1] - count1[i])
        else:
            res += count0[i-1] * (count0[n-1] - count0[i])
    return res

# Example usage:
# print(numberOfWays("001101"))  # Output: 6
