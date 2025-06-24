"""
LeetCode 1288. Remove Covered Intervals

Given a list of intervals, remove all intervals that are covered by another interval in the list. Return the number of remaining intervals.

Constraints:
- 1 <= intervals.length <= 1000
- intervals[i].length == 2
- 0 <= intervals[i][0] < intervals[i][1] <= 10^5

Example:
Input: intervals = [[1,4],[3,6],[2,8]]
Output: 2
"""
def removeCoveredIntervals(intervals):
    intervals.sort(key=lambda x: (x[0], -x[1]))
    res, end = 0, 0
    for _, e in intervals:
        if e > end:
            res += 1
            end = e
    return res

# Example usage:
intervals = [[1,4],[3,6],[2,8]]
print(removeCoveredIntervals(intervals))  # Output: 2
