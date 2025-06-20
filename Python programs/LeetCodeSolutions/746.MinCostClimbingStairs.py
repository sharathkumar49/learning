"""
LeetCode 746. Min Cost Climbing Stairs

You are given an integer array cost where cost[i] is the cost of i-th step on a staircase. Once you pay the cost, you can either climb one or two steps.
Return the minimum cost to reach the top of the floor.

Example 1:
Input: cost = [10,15,20]
Output: 15

Example 2:
Input: cost = [1,100,1,1,1,100,1,1,100,1]
Output: 6

Constraints:
- 2 <= cost.length <= 1000
- 0 <= cost[i] <= 999
"""
from typing import List

def minCostClimbingStairs(cost: List[int]) -> int:
    n = len(cost)
    dp = [0] * (n+1)
    for i in range(2, n+1):
        dp[i] = min(dp[i-1] + cost[i-1], dp[i-2] + cost[i-2])
    return dp[n]

# Example usage
if __name__ == "__main__":
    print(minCostClimbingStairs([10,15,20]))  # Output: 15
    print(minCostClimbingStairs([1,100,1,1,1,100,1,1,100,1]))  # Output: 6
