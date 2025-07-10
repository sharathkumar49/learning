"""
LeetCode 1882. Process Tasks Using Servers

You are given two integer arrays servers and tasks. Assign each task to the server with the least weight and earliest available time. Return the order of servers assigned to each task.

Example:
Input: servers = [3,3,2], tasks = [1,2,3,2,1,2]
Output: [2,2,0,2,1,2]

Constraints:
- 1 <= servers.length, tasks.length <= 2 * 10^5
- 1 <= servers[i], tasks[i] <= 2 * 10^5
"""

import heapq

def assignTasks(servers, tasks):
    n = len(servers)
    free = [(w, i) for i, w in enumerate(servers)]
    heapq.heapify(free)
    busy = []
    res = []
    time = 0
    for i, t in enumerate(tasks):
        time = max(time, i)
        while busy and busy[0][0] <= time:
            _, w, idx = heapq.heappop(busy)
            heapq.heappush(free, (w, idx))
        if not free:
            time = busy[0][0]
            while busy and busy[0][0] == time:
                _, w, idx = heapq.heappop(busy)
                heapq.heappush(free, (w, idx))
        w, idx = heapq.heappop(free)
        res.append(idx)
        heapq.heappush(busy, (time + t, w, idx))
    return res

# Example usage:
# print(assignTasks([3,3,2], [1,2,3,2,1,2]))  # Output: [2,2,0,2,1,2]
