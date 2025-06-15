# Program: Implement a Queue for Task Scheduling with Dependencies (Topological Sort)
# Problem: Given a list of tasks and dependencies, print a valid order to complete all tasks using a queue (Kahn's algorithm).
from collections import deque, defaultdict

def task_scheduling(tasks, dependencies):
    graph = defaultdict(list)
    indegree = {task: 0 for task in tasks}
    for pre, post in dependencies:
        graph[pre].append(post)
        indegree[post] += 1
    q = deque([task for task in tasks if indegree[task] == 0])
    order = []
    while q:
        curr = q.popleft()
        order.append(curr)
        for neighbor in graph[curr]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                q.append(neighbor)
    return order if len(order) == len(tasks) else []

if __name__ == '__main__':
    tasks = ['A', 'B', 'C', 'D', 'E', 'F']
    dependencies = [('A', 'D'), ('F', 'B'), ('B', 'D'), ('F', 'A'), ('D', 'C')]
    print(task_scheduling(tasks, dependencies))
