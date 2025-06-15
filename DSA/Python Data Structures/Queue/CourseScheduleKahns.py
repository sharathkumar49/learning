from collections import deque, defaultdict

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

def can_finish_courses(numCourses, prerequisites):
    graph = defaultdict(list)
    indegree = [0]*numCourses
    for u, v in prerequisites:
        graph[v].append(u)
        indegree[u] += 1
    q = Queue()
    for i in range(numCourses):
        if indegree[i] == 0:
            q.enqueue(i)
    count = 0
    while not q.is_empty():
        node = q.dequeue()
        count += 1
        for neighbor in graph[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                q.enqueue(neighbor)
    return count == numCourses

if __name__ == '__main__':
    numCourses = 4
    prerequisites = [(1,0),(2,1),(3,2)]
    print(can_finish_courses(numCourses, prerequisites))
