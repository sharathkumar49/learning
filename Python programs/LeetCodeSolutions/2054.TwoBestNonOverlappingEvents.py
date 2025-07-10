"""
LeetCode 2054. Two Best Non-Overlapping Events

Given a list of events, each with a start time, end time, and value, return the maximum sum of values of two non-overlapping events.

Example:
Input: events = [[1,3,4],[2,4,3],[3,10,2],[6,8,4]]
Output: 7

Constraints:
- 2 <= events.length <= 10^5
- 1 <= events[i][0] < events[i][1] <= 10^9
- 1 <= events[i][2] <= 10^6
"""

def maxTwoEvents(events):
    events.sort()
    import bisect
    n = len(events)
    max_val = [0] * n
    max_val[-1] = events[-1][2]
    for i in range(n-2, -1, -1):
        max_val[i] = max(events[i][2], max_val[i+1])
    res = 0
    for i, (s, e, v) in enumerate(events):
        idx = bisect.bisect_left(events, [e+1])
        if idx < n:
            res = max(res, v + max_val[idx])
        else:
            res = max(res, v)
    return res

# Example usage:
# print(maxTwoEvents([[1,3,4],[2,4,3],[3,10,2],[6,8,4]]))  # Output: 7
