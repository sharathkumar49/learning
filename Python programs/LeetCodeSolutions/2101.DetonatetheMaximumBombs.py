"""
LeetCode 2101. Detonate the Maximum Bombs

Given bombs with positions and radii, return the maximum number of bombs that can be detonated.

Example:
Input: bombs = [[2,1,3],[6,1,4]]
Output: 2

Constraints:
- 1 <= bombs.length <= 100
- 1 <= x, y, r <= 10^5
"""

def maximumDetonation(bombs):
    from collections import deque
    n = len(bombs)
    g = [[] for _ in range(n)]
    for i in range(n):
        x1, y1, r1 = bombs[i]
        for j in range(n):
            if i == j:
                continue
            x2, y2, _ = bombs[j]
            if (x1-x2)**2 + (y1-y2)**2 <= r1**2:
                g[i].append(j)
    def bfs(i):
        q = deque([i])
        seen = {i}
        while q:
            u = q.popleft()
            for v in g[u]:
                if v not in seen:
                    seen.add(v)
                    q.append(v)
        return len(seen)
    return max(bfs(i) for i in range(n))

# Example usage:
# print(maximumDetonation([[2,1,3],[6,1,4]]))  # Output: 2
