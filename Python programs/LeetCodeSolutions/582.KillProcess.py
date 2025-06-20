"""
582. Kill Process
Difficulty: Medium

Given n processes, each process has a unique PID (process id) and its PPID (parent process id).
Each process only has one parent process, but may have one or more children processes.
Given two integer arrays pid and ppid, and a process id to kill, return a list of PIDs of all processes that will be killed (including the given one).

Example 1:
Input: pid = [1,3,10,5], ppid = [3,0,5,3], kill = 5
Output: [5,10]

Constraints:
1 <= pid.length <= 5 * 10^4
ppid.length == pid.length
1 <= pid[i] <= 5 * 10^4
0 <= ppid[i] <= 5 * 10^4
kill is guaranteed to be one of pid.
"""

def killProcess(pid, ppid, kill):
    from collections import defaultdict, deque
    tree = defaultdict(list)
    for child, parent in zip(pid, ppid):
        tree[parent].append(child)
    res = []
    queue = deque([kill])
    while queue:
        curr = queue.popleft()
        res.append(curr)
        queue.extend(tree[curr])
    return res

# Example usage
if __name__ == "__main__":
    print(killProcess([1,3,10,5], [3,0,5,3], 5))  # Output: [5,10]
