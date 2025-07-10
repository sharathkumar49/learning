"""
LeetCode 1462. Course Schedule IV

There are a total of numCourses courses you have to take, labeled from 0 to numCourses-1. Some courses may have prerequisites. For a list of queries, return whether the first course is a prerequisite of the second course.

Constraints:
- 2 <= numCourses <= 100
- 0 <= prerequisites.length <= 100
- 0 <= ai, bi < numCourses
- 1 <= queries.length <= 100

Example:
Input: numCourses = 2, prerequisites = [[1,0]], queries = [[0,1],[1,0]]
Output: [false,true]
"""
def checkIfPrerequisite(numCourses, prerequisites, queries):
    reach = [[False]*numCourses for _ in range(numCourses)]
    for pre, course in prerequisites:
        reach[pre][course] = True
    for k in range(numCourses):
        for i in range(numCourses):
            for j in range(numCourses):
                reach[i][j] = reach[i][j] or (reach[i][k] and reach[k][j])
    return [reach[u][v] for u, v in queries]

# Example usage:
numCourses = 2
prerequisites = [[1,0]]
queries = [[0,1],[1,0]]
print(checkIfPrerequisite(numCourses, prerequisites, queries))  # Output: [False, True]
