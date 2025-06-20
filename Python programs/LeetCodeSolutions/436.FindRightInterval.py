"""
436. Find Right Interval

Given a set of intervals, for each interval i, find the minimum interval j such that interval i's end is greater than or equal to interval j's start.
Return an array of answers. If no such interval exists, put -1 instead.

Constraints:
- 1 <= intervals.length <= 2 * 10^4
- intervals[i].length == 2
- -10^6 <= start_i <= end_i <= 10^6

Example:
Input: intervals = [[1,2]]
Output: [-1]
"""

import bisect

class Solution:
    def findRightInterval(self, intervals: list) -> list:
        n = len(intervals)
        starts = sorted((iv[0], i) for i, iv in enumerate(intervals))
        res = []
        for iv in intervals:
            idx = bisect.bisect_left(starts, (iv[1],))
            res.append(starts[idx][1] if idx < n else -1)
        return res

# Example usage:
sol = Solution()
print(sol.findRightInterval([[1,2]]))  # Output: [-1]
