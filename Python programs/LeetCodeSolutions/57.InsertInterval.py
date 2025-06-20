# 57. Insert Interval
# You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] sorted by starti, and an interval newInterval = [start, end].
# Insert newInterval into intervals such that intervals is still sorted by starti and non-overlapping (merge if necessary).
#
# Example 1:
# Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
# Output: [[1,5],[6,9]]
#
# Example 2:
# Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
# Output: [[1,2],[3,10],[12,16]]
#
# Constraints:
# 0 <= intervals.length <= 10^4
# intervals[i].length == 2
# 0 <= starti <= endi <= 10^5
# newInterval.length == 2
# 0 <= start <= end <= 10^5

def insert(intervals, newInterval):
    res = []
    i = 0
    while i < len(intervals) and intervals[i][1] < newInterval[0]:
        res.append(intervals[i])
        i += 1
    while i < len(intervals) and intervals[i][0] <= newInterval[1]:
        newInterval[0] = min(newInterval[0], intervals[i][0])
        newInterval[1] = max(newInterval[1], intervals[i][1])
        i += 1
    res.append(newInterval)
    while i < len(intervals):
        res.append(intervals[i])
        i += 1
    return res

# Example usage
intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
newInterval = [4,8]
print("After insert:", insert(intervals, newInterval))  # Output: [[1,2],[3,10],[12,16]]
