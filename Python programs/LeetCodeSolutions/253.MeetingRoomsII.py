"""
253. Meeting Rooms II
https://leetcode.com/problems/meeting-rooms-ii/

Given an array of meeting time intervals intervals where intervals[i] = [starti, endi], return the minimum number of conference rooms required.

Constraints:
- 1 <= intervals.length <= 10^4
- 0 <= starti < endi <= 10^6

Example 1:
Input: intervals = [[0,30],[5,10],[15,20]]
Output: 2

Example 2:
Input: intervals = [[7,10],[2,4]]
Output: 1
"""
def minMeetingRooms(intervals):
    if not intervals:
        return 0
    starts = sorted(i[0] for i in intervals)
    ends = sorted(i[1] for i in intervals)
    s = e = 0
    used = 0
    res = 0
    while s < len(intervals):
        if starts[s] < ends[e]:
            used += 1
            res = max(res, used)
            s += 1
        else:
            used -= 1
            e += 1
    return res

# Example usage:
if __name__ == "__main__":
    print(minMeetingRooms([[0,30],[5,10],[15,20]]))  # Output: 2
    print(minMeetingRooms([[7,10],[2,4]]))           # Output: 1
