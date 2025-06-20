"""
983. Minimum Cost For Tickets
https://leetcode.com/problems/minimum-cost-for-tickets/

You have a list of days when you plan to travel and ticket costs for 1-day, 7-day, and 30-day passes. Return the minimum cost needed to travel for all the given days.

Constraints:
- 1 <= days.length <= 365
- 1 <= days[i] <= 365
- days is strictly increasing.
- costs.length == 3
- 1 <= costs[i] <= 1000

Example:
Input: days = [1,4,6,7,8,20], costs = [2,7,15]
Output: 11
"""
from typing import List

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        n = len(days)
        dp = [0] * (n+1)
        durations = [1, 7, 30]
        for i in range(n-1, -1, -1):
            dp[i] = float('inf')
            for d, c in zip(durations, costs):
                j = i
                while j < n and days[j] < days[i] + d:
                    j += 1
                dp[i] = min(dp[i], c + dp[j])
        return dp[0]

# Example usage
if __name__ == "__main__":
    days = [1,4,6,7,8,20]
    costs = [2,7,15]
    print(Solution().mincostTickets(days, costs))  # Output: 11
