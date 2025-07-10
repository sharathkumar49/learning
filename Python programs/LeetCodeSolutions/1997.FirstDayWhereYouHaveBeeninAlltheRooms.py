"""
LeetCode 1997. First Day Where You Have Been in All the Rooms

Given an array nextVisit, return the first day where you have been in all the rooms.

Example:
Input: nextVisit = [0,0]
Output: 2

Constraints:
- 1 <= nextVisit.length <= 10^5
- 0 <= nextVisit[i] < i+1
"""

def firstDayBeenInAllRooms(nextVisit):
    n = len(nextVisit)
    MOD = 10**9+7
    dp = [0]*n
    for i in range(1, n):
        dp[i] = (2*dp[i-1] - dp[nextVisit[i-1]] + 2) % MOD
    return dp[-1]

# Example usage:
# print(firstDayBeenInAllRooms([0,0]))  # Output: 2
