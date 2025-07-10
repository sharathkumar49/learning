"""
LeetCode 2055. Plates Between Candles

Given a string s and a list of queries, return the number of plates between candles for each query.

Example:
Input: s = "**|**|***|", queries = [[2,5],[5,9]]
Output: [2,3]

Constraints:
- 1 <= s.length <= 10^5
- 1 <= queries.length <= 10^5
"""

def platesBetweenCandles(s, queries):
    n = len(s)
    pre = [0] * (n+1)
    for i in range(n):
        pre[i+1] = pre[i] + (s[i] == '*')
    left = [-1] * n
    right = [-1] * n
    l = -1
    for i in range(n):
        if s[i] == '|':
            l = i
        left[i] = l
    r = -1
    for i in range(n-1, -1, -1):
        if s[i] == '|':
            r = i
        right[i] = r
    res = []
    for a, b in queries:
        l = right[a]
        r = left[b]
        if l != -1 and r != -1 and l < r:
            res.append(pre[r] - pre[l])
        else:
            res.append(0)
    return res

# Example usage:
# print(platesBetweenCandles("**|**|***|", [[2,5],[5,9]]))  # Output: [2,3]
