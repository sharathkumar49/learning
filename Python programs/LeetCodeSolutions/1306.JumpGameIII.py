"""
LeetCode 1306. Jump Game III

Given an array arr, you are initially positioned at start index. In one step you can jump to index i + arr[i] or i - arr[i]. Return true if you can reach any index with value 0.

Constraints:
- 1 <= arr.length <= 5 * 10^4
- 0 <= arr[i] < arr.length
- 0 <= start < arr.length

Example:
Input: arr = [4,2,3,0,3,1,2], start = 5
Output: true
"""
def canReach(arr, start):
    n = len(arr)
    visited = set()
    def dfs(i):
        if i < 0 or i >= n or i in visited:
            return False
        if arr[i] == 0:
            return True
        visited.add(i)
        return dfs(i + arr[i]) or dfs(i - arr[i])
    return dfs(start)

# Example usage:
arr = [4,2,3,0,3,1,2]
start = 5
print(canReach(arr, start))  # Output: True
