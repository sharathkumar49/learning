"""
1042. Flower Planting With No Adjacent

You have N gardens, each with some (possibly zero) paths between them. No garden has more than 3 paths. Return any such arrangement of flowers to gardens so that no two gardens connected by a path have the same type of flower.

Constraints:
- 1 <= N <= 10000
- 0 <= paths.length <= 20000
- paths[i].length == 2
- 1 <= paths[i][0], paths[i][1] <= N

Example:
Input: N = 3, paths = [[1,2],[2,3],[3,1]]
Output: [1,2,3]
"""
from typing import List

def gardenNoAdj(N: int, paths: List[List[int]]) -> List[int]:
    G = [[] for _ in range(N)]
    for x, y in paths:
        G[x-1].append(y-1)
        G[y-1].append(x-1)
    res = [0] * N
    for i in range(N):
        used = {res[j] for j in G[i]}
        for color in range(1, 5):
            if color not in used:
                res[i] = color
                break
    return res

# Example usage:
N = 3
paths = [[1,2],[2,3],[3,1]]
print(gardenNoAdj(N, paths))  # Output: [1, 2, 3]
