# Program: Implement a Queue for Rotten Tomatoes (Multi-Source BFS)
# Problem: Given a grid, find the minimum time to rot all fresh tomatoes using BFS (queue).
from collections import deque

class Queue:
    def __init__(self):
        self.buffer = deque()
    def enqueue(self, val):
        self.buffer.appendleft(val)
    def dequeue(self):
        return self.buffer.pop()
    def is_empty(self):
        return len(self.buffer)==0
    def size(self):
        return len(self.buffer)

def min_time_to_rot_tomatoes(grid):
    rows, cols = len(grid), len(grid[0])
    q = Queue()
    fresh = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 2:
                q.enqueue((r, c, 0))
            elif grid[r][c] == 1:
                fresh += 1
    time = 0
    while not q.is_empty():
        r, c, t = q.dequeue()
        for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
            nr, nc = r+dr, c+dc
            if 0<=nr<rows and 0<=nc<cols and grid[nr][nc]==1:
                grid[nr][nc]=2
                fresh -= 1
                q.enqueue((nr, nc, t+1))
                time = t+1
    return time if fresh==0 else -1

if __name__ == '__main__':
    grid = [[2,1,1],[1,1,0],[0,1,1]]
    print(min_time_to_rot_tomatoes(grid))
