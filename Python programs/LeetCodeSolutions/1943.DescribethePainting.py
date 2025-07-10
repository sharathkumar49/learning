"""
LeetCode 1943. Describe the Painting

Given a list of segments, return the list of non-overlapping intervals and the sum of colors in each interval.

Example:
Input: segments = [[1,4,5],[4,7,7],[1,7,9]]
Output: [[1,4,14],[4,7,16]]

Constraints:
- 1 <= segments.length <= 2 * 10^4
- segments[i].length == 3
- 1 <= segments[i][0] < segments[i][1] <= 10^5
- 1 <= segments[i][2] <= 10^5
"""

def splitPainting(segments):
    from collections import defaultdict
    events = defaultdict(int)
    for s, e, c in segments:
        events[s] += c
        events[e] -= c
    res = []
    prev = None
    color = 0
    for x in sorted(events):
        if prev is not None and color:
            res.append([prev, x, color])
        color += events[x]
        prev = x
    return res

# Example usage:
# print(splitPainting([[1,4,5],[4,7,7],[1,7,9]]))  # Output: [[1,4,14],[4,7,16]]
