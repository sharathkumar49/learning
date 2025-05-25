# Microsoft: Course Schedule II (Return Order)
# There are numCourses courses labeled from 0 to numCourses-1. Prerequisites are pairs [a, b] meaning to take course a you must first take course b.
# Return the order in which you should take the courses. If impossible, return [].
from collections import defaultdict, deque

def find_order(numCourses, prerequisites):
    graph = defaultdict(list)
    indegree = [0] * numCourses
    for a, b in prerequisites:
        graph[b].append(a)
        indegree[a] += 1
    queue = deque([i for i in range(numCourses) if indegree[i] == 0])
    order = []
    while queue:
        node = queue.popleft()
        order.append(node)
        for nei in graph[node]:
            indegree[nei] -= 1
            if indegree[nei] == 0:
                queue.append(nei)
    return order if len(order) == numCourses else []

if __name__ == "__main__":
    numCourses1 = 2
    prereq1 = [[1,0]]
    print(find_order(numCourses1, prereq1))  # Output: [0,1]
    numCourses2 = 4
    prereq2 = [[1,0],[2,0],[3,1],[3,2]]
    print(find_order(numCourses2, prereq2))  # Output: [0,2,1,3] or [0,1,2,3]
