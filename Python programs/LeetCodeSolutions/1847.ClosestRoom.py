"""
LeetCode 1847. Closest Room

You are given n rooms and a list of queries. Each room has a room_id and size. For each query [preferred, minSize], return the room_id of the room that has size >= minSize and is closest to preferred. If there are multiple, return the one with the smallest room_id. If no such room exists, return -1.

Example 1:
Input: rooms = [[2,3],[1,5],[3,3]], queries = [[3,3],[3,5],[3,2]]
Output: [3,1,3]

Constraints:
- 1 <= n <= 10^5
- 1 <= room_id, size, preferred, minSize <= 10^7
- 1 <= queries.length <= 10^5
"""

import bisect

def closestRoom(rooms, queries):
    rooms.sort(key=lambda x: -x[1])
    queries = sorted([(minSize, preferred, i) for i, (preferred, minSize) in enumerate(queries)], reverse=True)
    res = [-1]*len(queries)
    avail = []
    j = 0
    for minSize, preferred, idx in queries:
        while j < len(rooms) and rooms[j][1] >= minSize:
            bisect.insort(avail, rooms[j][0])
            j += 1
        i = bisect.bisect_left(avail, preferred)
        candidates = []
        if i < len(avail):
            candidates.append(avail[i])
        if i > 0:
            candidates.append(avail[i-1])
        if candidates:
            res[idx] = min(candidates, key=lambda x: (abs(x-preferred), x))
    return res

# Example usage:
# rooms = [[2,3],[1,5],[3,3]]
# queries = [[3,3],[3,5],[3,2]]
# print(closestRoom(rooms, queries))  # Output: [3,1,3]
