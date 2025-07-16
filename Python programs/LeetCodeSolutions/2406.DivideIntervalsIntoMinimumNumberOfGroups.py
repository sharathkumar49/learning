"""
LeetCode 2406. Divide Intervals Into Minimum Number of Groups

Given intervals, return the minimum number of groups to divide them into so that no intervals in a group overlap.

Constraints:
- 1 <= intervals.length <= 10^5
"""

def minGroups(intervals):
    intervals.sort()
    import heapq
    heap = []
    for s, e in intervals:
        if heap and heap[0] < s:
            heapq.heappop(heap)
        heapq.heappush(heap, e)
    return len(heap)

# Example usage:
# print(minGroups([[5,10],[6,8],[1,5],[2,3],[1,10]]))  # Output: 3
