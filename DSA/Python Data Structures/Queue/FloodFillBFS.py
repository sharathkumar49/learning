# Program: Implement a Queue for Flood Fill Algorithm (BFS)
# Problem: Use a queue to perform flood fill on a 2D grid (image).
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

def flood_fill(image, sr, sc, newColor):
    rows, cols = len(image), len(image[0])
    origColor = image[sr][sc]
    if origColor == newColor:
        return image
    q = Queue()
    q.enqueue((sr, sc))
    while not q.is_empty():
        r, c = q.dequeue()
        if image[r][c] == origColor:
            image[r][c] = newColor
            for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
                nr, nc = r+dr, c+dc
                if 0<=nr<rows and 0<=nc<cols and image[nr][nc]==origColor:
                    q.enqueue((nr, nc))
    return image

if __name__ == '__main__':
    image = [ [1,1,1], [1,1,0], [1,0,1] ]
    sr, sc, newColor = 1, 1, 2
    print(flood_fill(image, sr, sc, newColor))
