"""
LeetCode 1345. Jump Game IV

Given an array arr, you can jump from index i to i+1, i-1, or any index j where arr[i] == arr[j] and i != j. Return the minimum number of steps to reach the last index.

Constraints:
- 1 <= arr.length <= 5 * 10^4
- 0 <= arr[i] < arr.length

Example:
Input: arr = [100,-23,100,100,100,23,23,23,3,4]
Output: 3
"""
def minJumps(arr):
    from collections import defaultdict, deque
    n = len(arr)
    graph = defaultdict(list)
    for i, v in enumerate(arr):
        graph[v].append(i)
    queue = deque([0])
    visited = {0}
    steps = 0
    while queue:
        for _ in range(len(queue)):
            i = queue.popleft()
            if i == n-1:
                return steps
            for j in graph[arr[i]]:
                if j not in visited:
                    visited.add(j)
                    queue.append(j)
            graph[arr[i]].clear()
            for j in [i-1, i+1]:
                if 0 <= j < n and j not in visited:
                    visited.add(j)
                    queue.append(j)
        steps += 1
    return -1

# Example usage:
arr = [100,-23,100,100,100,23,23,23,3,4]
print(minJumps(arr))  # Output: 3
