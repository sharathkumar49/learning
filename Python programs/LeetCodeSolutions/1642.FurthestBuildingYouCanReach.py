"""
LeetCode 1642. Furthest Building You Can Reach

Given an array heights, an integer bricks, and an integer ladders, return the furthest building index you can reach by climbing with bricks and ladders.

Example 1:
Input: heights = [4,2,7,6,9,14,12], bricks = 5, ladders = 1
Output: 4

Constraints:
- 1 <= heights.length <= 10^5
- 0 <= bricks <= 10^9
- 0 <= ladders <= heights.length
"""

def furthestBuilding(heights, bricks, ladders):
    import heapq
    heap = []
    for i in range(len(heights)-1):
        d = heights[i+1] - heights[i]
        if d > 0:
            heapq.heappush(heap, d)
        if len(heap) > ladders:
            bricks -= heapq.heappop(heap)
        if bricks < 0:
            return i
    return len(heights)-1

# Example usage:
# heights = [4,2,7,6,9,14,12]
# bricks = 5
# ladders = 1
# print(furthestBuilding(heights, bricks, ladders))  # Output: 4
