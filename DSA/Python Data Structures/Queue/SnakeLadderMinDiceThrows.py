# Program: Implement a Queue for Snake and Ladder Minimum Dice Throws
# Problem: Find the minimum number of dice throws required to reach the last cell in a snake and ladder game using BFS (queue).

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

def min_dice_throws(moves, N):
    visited = [False]*N
    q = Queue()
    q.enqueue((0, 0))  # (cell, distance)
    visited[0] = True
    while not q.is_empty():
        v, dist = q.dequeue()
        if v == N-1:
            return dist
        for dice in range(1, 7):
            next_cell = v + dice
            if next_cell < N and not visited[next_cell]:
                visited[next_cell] = True
                if moves[next_cell] != -1:
                    q.enqueue((moves[next_cell], dist+1))
                else:
                    q.enqueue((next_cell, dist+1))
    return -1

if __name__ == '__main__':
    N = 30
    moves = [-1]*N
    moves[2] = 21
    moves[4] = 7
    moves[10] = 25
    moves[19] = 28
    moves[26] = 0
    moves[20] = 8
    moves[16] = 3
    moves[18] = 6
    print(min_dice_throws(moves, N))
