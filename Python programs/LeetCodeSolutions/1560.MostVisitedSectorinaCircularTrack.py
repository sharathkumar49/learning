"""
LeetCode 1560. Most Visited Sector in a Circular Track

Given an integer n and an array rounds, return the most visited sectors in the track in ascending order.

Constraints:
- 2 <= n <= 100
- 1 <= rounds.length <= 100
- 1 <= rounds[i] <= n

Example:
Input: n = 4, rounds = [1,3,1,2]
Output: [1,2]
"""
def mostVisited(n, rounds):
    res = []
    start, end = rounds[0], rounds[-1]
    if start <= end:
        res = list(range(start, end+1))
    else:
        res = list(range(1, end+1)) + list(range(start, n+1))
    return res

# Example usage:
n = 4
rounds = [1,3,1,2]
print(mostVisited(n, rounds))  # Output: [1, 2]
