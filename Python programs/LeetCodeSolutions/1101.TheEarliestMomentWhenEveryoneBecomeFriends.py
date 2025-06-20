"""
1101. The Earliest Moment When Everyone Become Friends

There are N people in a social group. Each log contains a timestamp and two people who became friends. Return the earliest time when everyone became friends. If it is impossible, return -1.

Constraints:
- 1 <= N <= 100
- 1 <= logs.length <= N * (N - 1) / 2
- logs[i].length == 3
- 0 <= logs[i][0] <= 10^9
- 0 <= logs[i][1], logs[i][2] < N

Example:
Input: logs = [[20190101,0,1],[20190104,3,4],[20190107,2,3],[20190211,1,5],[20190224,2,4],[20190301,0,3],[20190312,1,2],[20190322,4,5]], N = 6
Output: 20190301
"""
from typing import List

def earliestAcq(logs: List[List[int]], N: int) -> int:
    logs.sort()
    parent = list(range(N))
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    count = N
    for t, a, b in logs:
        pa, pb = find(a), find(b)
        if pa != pb:
            parent[pa] = pb
            count -= 1
            if count == 1:
                return t
    return -1

# Example usage:
logs = [[20190101,0,1],[20190104,3,4],[20190107,2,3],[20190211,1,5],[20190224,2,4],[20190301,0,3],[20190312,1,2],[20190322,4,5]]
N = 6
print(earliestAcq(logs, N))  # Output: 20190301
