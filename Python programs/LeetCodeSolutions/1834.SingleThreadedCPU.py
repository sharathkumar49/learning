"""
LeetCode 1834. Single-Threaded CPU

Given a list of tasks, each with an enqueue time and processing time, return the order in which the CPU will process the tasks.

Example 1:
Input: tasks = [[1,2],[2,4],[3,2],[4,1]]
Output: [0,2,3,1]

Constraints:
- 1 <= tasks.length <= 10^5
- 1 <= enqueueTimei, processingTimei <= 10^9
"""

def getOrder(tasks):
    import heapq
    tasks = sorted([(et, pt, i) for i, (et, pt) in enumerate(tasks)])
    res = []
    h = []
    time = 0
    i = 0
    n = len(tasks)
    while i < n or h:
        if not h and time < tasks[i][0]:
            time = tasks[i][0]
        while i < n and tasks[i][0] <= time:
            heapq.heappush(h, (tasks[i][1], tasks[i][2]))
            i += 1
        pt, idx = heapq.heappop(h)
        time += pt
        res.append(idx)
    return res

# Example usage:
# tasks = [[1,2],[2,4],[3,2],[4,1]]
# print(getOrder(tasks))  # Output: [0,2,3,1]
