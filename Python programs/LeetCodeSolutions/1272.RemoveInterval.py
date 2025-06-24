"""
LeetCode 1272. Remove Interval

Given a sorted list of non-overlapping intervals and an interval to remove, return the resulting list of intervals after removing the given interval.

Constraints:
- 1 <= intervals.length <= 10^4
- intervals[i].length == 2
- 0 <= intervals[i][0] < intervals[i][1] <= 10^9
- 0 <= toBeRemoved[0] < toBeRemoved[1] <= 10^9

Example:
Input: intervals = [[0,2],[3,4],[5,7]], toBeRemoved = [1,6]
Output: [[0,1],[6,7]]

"""
def removeInterval(intervals, toBeRemoved):
    res = []
    for start, end in intervals:
        if end <= toBeRemoved[0] or start >= toBeRemoved[1]:
            res.append([start, end])
        else:
            if start < toBeRemoved[0]:
                res.append([start, toBeRemoved[0]])
            if end > toBeRemoved[1]:
                res.append([toBeRemoved[1], end])
    return res

# Example usage:
intervals = [[0,2],[3,4],[5,7]]
toBeRemoved = [1,6]
print(removeInterval(intervals, toBeRemoved))  # Output: [[0,1],[6,7]]
