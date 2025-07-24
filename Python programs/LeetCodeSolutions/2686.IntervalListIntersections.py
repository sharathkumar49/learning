"""
LeetCode 2686. Interval List Intersections

Given two lists of intervals, return their intersection.

Constraints:
- 1 <= firstList.length, secondList.length <= 10^5
"""

def intervalIntersection(firstList, secondList):
    res = []
    i = j = 0
    while i < len(firstList) and j < len(secondList):
        a, b = firstList[i], secondList[j]
        lo = max(a[0], b[0])
        hi = min(a[1], b[1])
        if lo <= hi:
            res.append([lo, hi])
        if a[1] < b[1]:
            i += 1
        else:
            j += 1
    return res
# Example usage:
# print(intervalIntersection([[0,2],[5,10],[13,23],[24,25]], [[1,5],[8,12],[15,24],[25,26]]))  # Output: [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
