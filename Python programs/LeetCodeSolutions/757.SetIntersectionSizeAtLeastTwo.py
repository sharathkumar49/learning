"""
LeetCode 757. Set Intersection Size At Least Two

An integer interval [a, b] (for a <= b) is a set of all integers from a to b, inclusive.
A set S is a set intersection size at least two if for every interval [a, b], |S ∩ [a, b]| >= 2.
Return the minimum size of such a set S.

Example 1:
Input: intervals = [[1,3],[1,4],[2,5],[3,5]]
Output: 3

Example 2:
Input: intervals = [[1,2],[2,3],[2,4],[4,5]]
Output: 5

Constraints:
- 1 <= intervals.length <= 3000
- intervals[i].length == 2
- 0 <= intervals[i][0] < intervals[i][1] <= 10^8
"""
from typing import List

def intersectionSizeTwo(intervals: List[List[int]]) -> int:
    intervals.sort(key=lambda x: (x[1], -x[0]))
    res = 0
    s = []
    for a, b in intervals:
        cnt = 0
        for x in reversed(s):
            if a <= x <= b:
                cnt += 1
            if cnt == 2:
                break
        for x in range(b, a-1, -1):
            if cnt == 2:
                break
            if x not in s:
                s.append(x)
                res += 1
                cnt += 1
    return res

# Example usage
if __name__ == "__main__":
    print(intersectionSizeTwo([[1,3],[1,4],[2,5],[3,5]]))  # Output: 3
    print(intersectionSizeTwo([[1,2],[2,3],[2,4],[4,5]]))  # Output: 5
