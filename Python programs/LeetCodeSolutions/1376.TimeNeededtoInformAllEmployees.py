"""
LeetCode 1376. Time Needed to Inform All Employees

A company has n employees with a head and a manager array. Each employee needs informTime[i] minutes to inform their subordinates. Return the time needed to inform all employees.

Constraints:
- 1 <= n <= 10^5
- 0 <= manager[i] < n or manager[i] == -1
- 0 <= informTime[i] <= 100

Example:
Input: n = 6, headID = 2, manager = [2,2,-1,2,2,2], informTime = [0,0,1,0,0,0]
Output: 1
"""
def numOfMinutes(n, headID, manager, informTime):
    from collections import defaultdict
    tree = defaultdict(list)
    for i, m in enumerate(manager):
        if m != -1:
            tree[m].append(i)
    def dfs(u):
        return max([dfs(v) for v in tree[u]] or [0]) + informTime[u]
    return dfs(headID)

# Example usage:
n = 6
headID = 2
manager = [2,2,-1,2,2,2]
informTime = [0,0,1,0,0,0]
print(numOfMinutes(n, headID, manager, informTime))  # Output: 1
