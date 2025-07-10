"""
LeetCode 1751. Maximum Number of Events That Can Be Attended II

Given a list of events, each with a start day, end day, and value, and an integer k, return the maximum sum of values by attending at most k non-overlapping events.

Example 1:
Input: events = [[1,2,4],[3,4,3],[2,3,1]], k = 2
Output: 7

Constraints:
- 1 <= k <= events.length <= 10^4
- 1 <= starti <= endi <= 10^9
- 1 <= valuei <= 10^6
"""

def maxValue(events, k):
    import bisect
    events.sort(key=lambda x: x[1])
    n = len(events)
    dp = [[0]*(k+1) for _ in range(n+1)]
    starts = [e[0] for e in events]
    for i in range(1, n+1):
        s, e, v = events[i-1]
        idx = bisect.bisect_right([ev[1] for ev in events], s-1, 0, i-1)
        for j in range(1, k+1):
            dp[i][j] = max(dp[i-1][j], dp[idx][j-1] + v)
    return dp[n][k]

# Example usage:
# events = [[1,2,4],[3,4,3],[2,3,1]]
# k = 2
# print(maxValue(events, k))  # Output: 7
