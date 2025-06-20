"""
218. The Skyline Problem
https://leetcode.com/problems/the-skyline-problem/

A city's skyline is the outer contour of the silhouette formed by all the buildings in that city when viewed from a distance.
Given the locations and heights of all the buildings, return the skyline formed by these buildings collectively.

Each building is represented by a triplet [left, right, height]:
- left is the x coordinate of the left edge of the building.
- right is the x coordinate of the right edge of the building.
- height is the height of the building.

Return the skyline as a list of "key points" sorted by their x-coordinate.

Constraints:
- 1 <= buildings.length <= 10^4
- 0 <= left < right <= 2^31 - 1
- 1 <= height <= 2^31 - 1

Example 1:
Input: buildings = [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]
Output: [[2,10],[3,15],[7,12],[12,0],[15,10],[20,8],[24,0]]

Example 2:
Input: buildings = [[0,2,3],[2,5,3]]
Output: [[0,3],[5,0]]
"""
import heapq

def getSkyline(buildings):
    events = []
    for l, r, h in buildings:
        events.append((l, -h, r))
        events.append((r, 0, 0))
    events.sort()
    res = [[0, 0]]
    heap = [(0, float('inf'))]
    for x, neg_h, r in events:
        while heap[0][1] <= x:
            heapq.heappop(heap)
        if neg_h:
            heapq.heappush(heap, (neg_h, r))
        if res[-1][1] != -heap[0][0]:
            res.append([x, -heap[0][0]])
    return res[1:]

# Example usage:
if __name__ == "__main__":
    print(getSkyline([[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]))
    # Output: [[2,10],[3,15],[7,12],[12,0],[15,10],[20,8],[24,0]]
    print(getSkyline([[0,2,3],[2,5,3]]))
    # Output: [[0,3],[5,0]]
