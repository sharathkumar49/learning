"""
LeetCode 1851. Minimum Interval to Include Each Query

You are given an array of intervals and an array of queries. For each query, return the size of the smallest interval that contains that query. If no interval contains the query, return -1.

Example 1:
Input: intervals = [[1,4],[2,4],[3,6],[4,4]], queries = [2,3,4,5]
Output: [3,3,1,4]

Constraints:
- 1 <= intervals.length, queries.length <= 10^5
- intervals[i].length == 2
- 1 <= intervals[i][0] <= intervals[i][1] <= 10^7
- 1 <= queries[i] <= 10^7
"""

import heapq

def minInterval(intervals, queries):
    intervals.sort()
    res = [-1]*len(queries)
    h = []
    i = 0
    q = sorted([(v, idx) for idx, v in enumerate(queries)])
    for v, idx in q:
        while i < len(intervals) and intervals[i][0] <= v:
            l, r = intervals[i]
            heapq.heappush(h, (r-l+1, r))
            i += 1
        while h and h[0][1] < v:
            heapq.heappop(h)
        if h:
            res[idx] = h[0][0]
    return res

# Example usage:
# intervals = [[1,4],[2,4],[3,6],[4,4]]
# queries = [2,3,4,5]
# print(minInterval(intervals, queries))  # Output: [3,3,1,4]
