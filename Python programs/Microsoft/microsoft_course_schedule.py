# Microsoft: Course Schedule (Detect Cycle in Directed Graph)
# There are numCourses courses labeled from 0 to numCourses-1. Prerequisites are pairs [a, b] meaning to take course a you must first take course b.
# Return True if you can finish all courses (i.e., no cycle), else False.
from collections import defaultdict, deque

def can_finish(numCourses, prerequisites):
    graph = defaultdict(list)
    indegree = [0] * numCourses
    for a, b in prerequisites:
        graph[b].append(a)
        indegree[a] += 1
    queue = deque([i for i in range(numCourses) if indegree[i] == 0])
    count = 0
    while queue:
        node = queue.popleft()
        count += 1
        for nei in graph[node]:
            indegree[nei] -= 1
            if indegree[nei] == 0:
                queue.append(nei)
    return count == numCourses

if __name__ == "__main__":
    numCourses1 = 2
    prereq1 = [[1,0]]
    print(can_finish(numCourses1, prereq1))  # True
    numCourses2 = 2
    prereq2 = [[1,0],[0,1]]
    print(can_finish(numCourses2, prereq2))  # False
    numCourses3 = 4
    prereq3 = [[1,0],[2,1],[3,2]]
    print(can_finish(numCourses3, prereq3))  # True
