"""
252. Meeting Rooms
https://leetcode.com/problems/meeting-rooms/

Given an array of meeting time intervals intervals where intervals[i] = [starti, endi], determine if a person could attend all meetings.

Constraints:
- 0 <= intervals.length <= 10^4
- 0 <= starti < endi <= 10^6

Example 1:
Input: intervals = [[0,30],[5,10],[15,20]]
Output: false

Example 2:
Input: intervals = [[7,10],[2,4]]
Output: true
"""
def canAttendMeetings(intervals):
    intervals.sort()
    for i in range(1, len(intervals)):
        if intervals[i][0] < intervals[i-1][1]:
            return False
    return True

# Example usage:
if __name__ == "__main__":
    print(canAttendMeetings([[0,30],[5,10],[15,20]]))  # Output: False
    print(canAttendMeetings([[7,10],[2,4]]))           # Output: True
