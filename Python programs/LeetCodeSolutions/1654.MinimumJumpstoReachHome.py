"""
LeetCode 1654. Minimum Jumps to Reach Home

Given integers forbidden, a, b, x, return the minimum number of jumps needed to reach x starting from 0. You can jump forward by a, backward by b, but cannot land on forbidden positions or go below 0.

Example 1:
Input: forbidden = [14,4,18,1,15], a = 3, b = 15, x = 9
Output: 3

Constraints:
- 1 <= forbidden.length <= 1000
- 1 <= a, b, x <= 2000
- 0 <= forbidden[i] <= 2000
"""

def minimumJumps(forbidden, a, b, x):
    from collections import deque
    forbidden = set(forbidden)
    q = deque([(0, 0, True)])
    seen = set([(0, True)])
    upper = 6000
    steps = 0
    while q:
        for _ in range(len(q)):
            pos, back, can_back = q.popleft()
            if pos == x:
                return steps
            for nxt, new_can_back in ((pos+a, True), (pos-b, False)):
                if 0 <= nxt <= upper and nxt not in forbidden and (nxt, new_can_back) not in seen:
                    if new_can_back or can_back:
                        if nxt != pos-b or can_back:
                            q.append((nxt, steps+1, new_can_back))
                            seen.add((nxt, new_can_back))
        steps += 1
    return -1

# Example usage:
# forbidden = [14,4,18,1,15]
# a = 3
# b = 15
# x = 9
# print(minimumJumps(forbidden, a, b, x))  # Output: 3
