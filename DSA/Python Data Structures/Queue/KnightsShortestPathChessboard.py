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

def is_inside(x, y, N):
    return 0 <= x < N and 0 <= y < N

def knight_shortest_path(N, start, end):
    moves = [(-2, -1), (-1, -2), (1, -2), (2, -1),
             (2, 1), (1, 2), (-1, 2), (-2, 1)]
    visited = [[False]*N for _ in range(N)]
    q = Queue()
    q.enqueue((start[0], start[1], 0))
    visited[start[0]][start[1]] = True
    while not q.is_empty():
        x, y, dist = q.dequeue()
        if (x, y) == end:
            return dist
        for dx, dy in moves:
            nx, ny = x + dx, y + dy
            if is_inside(nx, ny, N) and not visited[nx][ny]:
                visited[nx][ny] = True
                q.enqueue((nx, ny, dist+1))
    return -1

if __name__ == '__main__':
    N = 8
    start = (0, 0)
    end = (7, 7)
    print(knight_shortest_path(N, start, end))
