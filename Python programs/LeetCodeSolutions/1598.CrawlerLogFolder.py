"""
LeetCode 1598. Crawler Log Folder

The folder structure is represented as a string array logs. Each log is one of the following:
- "../" : Move to the parent folder.
- "./" : Stay in the current folder.
- "x/" : Move to the child folder named x.

Return the minimum number of operations needed to go back to the main folder after the sequence of operations.

Example 1:
Input: logs = ["d1/","d2/","../","d21/","./"]
Output: 2

Constraints:
- 1 <= logs.length <= 300
- logs[i] == "../" or logs[i] == "./" or logs[i] matches the format "x/".
"""

def minOperations(logs):
    depth = 0
    for log in logs:
        if log == '../':
            if depth > 0:
                depth -= 1
        elif log != './':
            depth += 1
    return depth

# Example usage:
# logs = ["d1/","d2/","../","d21/","./"]
# print(minOperations(logs))  # Output: 2
