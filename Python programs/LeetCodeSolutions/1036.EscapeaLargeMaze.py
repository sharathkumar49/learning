"""
1036. Escape a Large Maze

There is a 1 million by 1 million grid with some blocked cells. You are given the list of blocked cells and two points: source and target. Return true if it is possible to reach the target from the source without passing through any blocked cell.

Constraints:
- 0 <= blocked.length <= 200
- blocked[i].length == 2
- 0 <= blocked[i][j] < 10^6
- source.length == target.length == 2
- source[i].length == target[i].length == 2

Example:
Input: blocked = [[0,1],[1,0]], source = [0,0], target = [0,2]
Output: false
"""
from typing import List

def isEscapePossible(blocked: List[List[int]], source: List[int], target: List[int]) -> bool:
    BLOCKED, VALID = -1, 0
    n = 10 ** 6
    blocked_set = {tuple(p) for p in blocked}
    max_area = len(blocked) * (len(blocked) - 1) // 2
    def bfs(start, finish):
        seen = {tuple(start)}
        queue = [start]
        for _ in range(max_area):
            if not queue:
                return False
            x, y = queue.pop(0)
            for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < n and (nx, ny) not in blocked_set and (nx, ny) not in seen:
                    if [nx, ny] == finish:
                        return True
                    seen.add((nx, ny))
                    queue.append([nx, ny])
        return True
    return bfs(source, target) and bfs(target, source)

# Example usage:
blocked = [[0,1],[1,0]]
source = [0,0]
target = [0,2]
print(isEscapePossible(blocked, source, target))  # Output: False
