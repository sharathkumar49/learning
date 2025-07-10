"""
LeetCode 1868. Merge Intervals

You are given two lists of closed intervals, each list of intervals is pairwise disjoint and in sorted order. Return the intersection of these two interval lists.

Example:
Input: firstList = [[0,2],[5,10],[13,23],[24,25]], secondList = [[1,5],[8,12],[15,24],[25,26]]
Output: [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]

Constraints:
- 0 <= firstList.length, secondList.length <= 1000
- 0 <= start_i < end_i <= 10^9
"""

def intervalIntersection(A, B):
    res = []
    i = j = 0
    while i < len(A) and j < len(B):
        lo = max(A[i][0], B[j][0])
        hi = min(A[i][1], B[j][1])
        if lo <= hi:
            res.append([lo, hi])
        if A[i][1] < B[j][1]:
            i += 1
        else:
            j += 1
    return res

# Example usage:
A = [[0,2],[5,10],[13,23],[24,25]]
B = [[1,5],[8,12],[15,24],[25,26]]
print(intervalIntersection(A, B))  # Output: [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
