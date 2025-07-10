"""
LeetCode 1583. Count Unhappy Friends

Given a list of n friends and their preferences, and a list of pairs denoting who is paired with whom, return the number of unhappy friends.

A friend x is unhappy if there exists a friend y such that x prefers y over their current partner, and y prefers x over their current partner.

Example 1:
Input: n = 4, preferences = [[1,2,3],[3,2,0],[3,1,0],[1,2,0]], pairs = [[0,1],[2,3]]
Output: 2

Constraints:
- 2 <= n <= 500
- preferences.length == n
- pairs.length == n / 2
"""

def unhappyFriends(n, preferences, pairs):
    order = [[0]*n for _ in range(n)]
    for i in range(n):
        for j, v in enumerate(preferences[i]):
            order[i][v] = j
    match = [0]*n
    for x, y in pairs:
        match[x] = y
        match[y] = x
    res = 0
    for x in range(n):
        y = match[x]
        idx = order[x][y]
        for u in preferences[x][:idx]:
            v = match[u]
            if order[u][x] < order[u][v]:
                res += 1
                break
    return res

# Example usage:
# n = 4
# preferences = [[1,2,3],[3,2,0],[3,1,0],[1,2,0]]
# pairs = [[0,1],[2,3]]
# print(unhappyFriends(n, preferences, pairs))  # Output: 2
