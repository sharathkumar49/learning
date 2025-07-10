"""
LeetCode 2188. Minimum Time to Finish the Race

Given an array of tire types, each with a starting lap time and an increase factor, and an integer changeTime and numLaps, return the minimum time to finish the race.

Example:
Input: tires = [[2,3],[3,4]], changeTime = 5, numLaps = 4
Output: 21

Constraints:
- 1 <= tires.length <= 10^5
- 1 <= changeTime, numLaps <= 10^5
- 1 <= f <= 10^5
"""

def minimumFinishTime(tires, changeTime, numLaps):
    import math
    n = len(tires)
    min_lap = [math.inf] * (numLaps+1)
    for f, r in tires:
        t = f
        total = 0
        for k in range(1, numLaps+1):
            total += t
            if total > 2e9: break
            min_lap[k] = min(min_lap[k], total)
            t *= r
    dp = [math.inf] * (numLaps+1)
    dp[0] = 0
    for i in range(1, numLaps+1):
        for k in range(1, min(i, 20)+1):
            dp[i] = min(dp[i], dp[i-k] + min_lap[k] + (0 if i==k else changeTime))
    return dp[numLaps]

# Example usage:
# print(minimumFinishTime([[2,3],[3,4]], 5, 4))  # Output: 21
