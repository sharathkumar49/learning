"""
LeetCode 752. Open the Lock

You have a lock in front of you with 4 circular wheels. Each wheel has 10 slots: '0' to '9'. The lock starts at '0000', a string representing the state of the wheels.
You are given a list of deadends, meaning if the lock displays any of these codes, the wheels will stop turning and you will be unable to open it.
Given a target representing the code you want to open, return the minimum total number of turns required to open the lock, or -1 if it is impossible.

Example 1:
Input: deadends = ["0201","0101","0102","1212","2002"], target = "0202"
Output: 6

Example 2:
Input: deadends = ["8888"], target = "0009"
Output: 1

Constraints:
- 1 <= deadends.length <= 500
- deadends[i].length == 4
- target.length == 4
- target will not be in the list deadends.
- '0000' will not be in the list deadends.
"""
from typing import List
from collections import deque

def openLock(deadends: List[str], target: str) -> int:
    dead = set(deadends)
    queue = deque([('0000', 0)])
    seen = {'0000'}
    while queue:
        node, depth = queue.popleft()
        if node == target:
            return depth
        if node in dead:
            continue
        for i in range(4):
            for d in [-1, 1]:
                nxt = node[:i] + str((int(node[i]) + d) % 10) + node[i+1:]
                if nxt not in seen and nxt not in dead:
                    seen.add(nxt)
                    queue.append((nxt, depth+1))
    return -1

# Example usage
if __name__ == "__main__":
    print(openLock(["0201","0101","0102","1212","2002"], "0202"))  # Output: 6
    print(openLock(["8888"], "0009"))  # Output: 1
