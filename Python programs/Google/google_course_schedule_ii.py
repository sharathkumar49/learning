# Google: Course Schedule II
# There are a total of numCourses you have to take, labeled from 0 to numCourses-1. Some courses may have prerequisites. Return the order in which you should take the courses.
from collections import defaultdict, deque

def find_order(numCourses, prerequisites):
    graph = defaultdict(list)
    indegree = [0] * numCourses
    for dest, src in prerequisites:
        graph[src].append(dest)
        indegree[dest] += 1
    queue = deque([i for i in range(numCourses) if indegree[i] == 0])
    order = []
    while queue:
        node = queue.popleft()
        order.append(node)
        for neighbor in graph[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)
    return order if len(order) == numCourses else []

if __name__ == "__main__":
    print(find_order(2, [[1,0]]))        # Output: [0,1]
    print(find_order(4, [[1,0],[2,0],[3,1],[3,2]])) # Output: [0,2,1,3] or [0,1,2,3]
