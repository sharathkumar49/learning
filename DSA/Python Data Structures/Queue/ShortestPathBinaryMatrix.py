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

def shortest_path_binary_matrix(grid):
    n = len(grid)
    if grid[0][0] != 0 or grid[n-1][n-1] != 0:
        return -1
    q = Queue()
    q.enqueue((0, 0, 1))
    visited = set((0, 0))
    directions = [(-1,0),(1,0),(0,-1),(0,1),(-1,-1),(-1,1),(1,-1),(1,1)]
    while not q.is_empty():
        x, y, dist = q.dequeue()
        if (x, y) == (n-1, n-1):
            return dist
        for dx, dy in directions:
            nx, ny = x+dx, y+dy
            if 0<=nx<n and 0<=ny<n and grid[nx][ny]==0 and (nx,ny) not in visited:
                visited.add((nx,ny))
                q.enqueue((nx,ny,dist+1))
    return -1

if __name__ == '__main__':
    grid = [
        [0,1,1,0],
        [1,0,1,1],
        [1,1,0,0],
        [1,1,1,0]
    ]
    print(shortest_path_binary_matrix(grid))
