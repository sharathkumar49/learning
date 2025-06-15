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

def jump_game_ii(nums):
    n = len(nums)
    if n <= 1:
        return 0
    q = Queue()
    q.enqueue((0, 0))  # (index, jumps)
    visited = set([0])
    while not q.is_empty():
        idx, jumps = q.dequeue()
        for next_idx in range(idx+1, min(idx+nums[idx]+1, n)):
            if next_idx == n-1:
                return jumps+1
            if next_idx not in visited:
                visited.add(next_idx)
                q.enqueue((next_idx, jumps+1))
    return -1

if __name__ == '__main__':
    nums = [2,3,1,1,4]
    print(jump_game_ii(nums))
