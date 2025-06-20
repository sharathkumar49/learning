"""
986. Interval List Intersections
https://leetcode.com/problems/interval-list-intersections/

You are given two lists of closed intervals, firstList and secondList, each list of disjoint intervals sorted by start time. Return the intersection of these two interval lists.

Constraints:
- 0 <= firstList.length, secondList.length <= 1000
- firstList[i].length == 2, secondList[j].length == 2
- 0 <= firstList[i][0] <= firstList[i][1] <= 10^9
- 0 <= secondList[j][0] <= secondList[j][1] <= 10^9

Example:
Input: firstList = [[0,2],[5,10],[13,23],[24,25]], secondList = [[1,5],[8,12],[15,24],[25,26]]
Output: [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
"""
from typing import List

class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        res = []
        i = j = 0
        while i < len(firstList) and j < len(secondList):
            a_start, a_end = firstList[i]
            b_start, b_end = secondList[j]
            start = max(a_start, b_start)
            end = min(a_end, b_end)
            if start <= end:
                res.append([start, end])
            if a_end < b_end:
                i += 1
            else:
                j += 1
        return res

# Example usage
if __name__ == "__main__":
    firstList = [[0,2],[5,10],[13,23],[24,25]]
    secondList = [[1,5],[8,12],[15,24],[25,26]]
    print(Solution().intervalIntersection(firstList, secondList))
    # Output: [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
