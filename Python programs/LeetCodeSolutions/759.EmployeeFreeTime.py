"""
LeetCode 759. Employee Free Time

We are given a list schedule, where schedule[i] is a list of non-overlapping intervals representing the working time for employee i.
Return the list of finite intervals representing common, positive-length free time for all employees, also in sorted order.

Example 1:
Input: schedule = [[[1,2],[5,6]],[[1,3]],[[4,10]]]
Output: [[3,4]]

Constraints:
- 1 <= schedule.length <= 50
- 1 <= schedule[i].length <= 50
- schedule[i][j].length == 2
- 0 <= schedule[i][j][0] < schedule[i][j][1] <= 10^8
"""
from typing import List

class Interval:
    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end

def employeeFreeTime(schedule: List[List[Interval]]) -> List[List[int]]:
    times = []
    for emp in schedule:
        for iv in emp:
            times.append((iv.start, iv.end))
    times.sort()
    res = []
    prev_end = times[0][1]
    for s, e in times[1:]:
        if s > prev_end:
            res.append([prev_end, s])
        prev_end = max(prev_end, e)
    return res

# Example usage
if __name__ == "__main__":
    schedule = [ [Interval(1,2),Interval(5,6)], [Interval(1,3)], [Interval(4,10)] ]
    print(employeeFreeTime(schedule))  # Output: [[3,4]]
