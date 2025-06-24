"""
LeetCode 1289. Minimum Falling Path Sum II

Given a square grid of integers, return the minimum sum of a falling path with non-zero shifts (no two elements chosen from the same column in consecutive rows).

Constraints:
- 1 <= arr.length == arr[i].length <= 200
- -99 <= arr[i][j] <= 99

Example:
Input: arr = [[1,2,3],[4,5,6],[7,8,9]]
Output: 13
"""
def minFallingPathSum(arr):
    n = len(arr)
    dp = arr[0][:]
    for i in range(1, n):
        new_dp = [float('inf')] * n
        for j in range(n):
            for k in range(n):
                if k != j:
                    new_dp[j] = min(new_dp[j], dp[k] + arr[i][j])
        dp = new_dp
    return min(dp)

# Example usage:
arr = [[1,2,3],[4,5,6],[7,8,9]]
print(minFallingPathSum(arr))  # Output: 13
