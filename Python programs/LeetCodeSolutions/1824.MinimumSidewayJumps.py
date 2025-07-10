"""
LeetCode 1824. Minimum Sideway Jumps

Given an array obstacles, return the minimum number of sideway jumps to reach the end.

Example 1:
Input: obstacles = [0,1,2,3,0]
Output: 2

Constraints:
- 2 <= obstacles.length <= 5 * 10^5
- 0 <= obstacles[i] <= 3
"""

def minSideJumps(obstacles):
    n = len(obstacles)
    dp = [1, 0, 1]
    for i in range(1, n):
        for j in range(3):
            if obstacles[i] == j+1:
                dp[j] = float('inf')
        min_dp = min(dp)
        for j in range(3):
            if obstacles[i] != j+1:
                dp[j] = min(dp[j], min_dp+1)
    return min(dp)

# Example usage:
# obstacles = [0,1,2,3,0]
# print(minSideJumps(obstacles))  # Output: 2
