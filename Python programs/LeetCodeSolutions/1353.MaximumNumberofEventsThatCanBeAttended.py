"""
LeetCode 1353. Maximum Number of Events That Can Be Attended

Given an array events where events[i] = [startDay, endDay], return the maximum number of events you can attend. You can only attend one event per day.

Constraints:
- 1 <= events.length <= 10^5
- 1 <= startDay <= endDay <= 10^5

Example:
Input: events = [[1,2],[2,3],[3,4]]
Output: 3
"""
def maxEvents(events):
    import heapq
    events.sort()
    res = day = i = 0
    h = []
    n = len(events)
    while h or i < n:
        if not h:
            day = events[i][0]
        while i < n and events[i][0] == day:
            heapq.heappush(h, events[i][1])
            i += 1
        heapq.heappop(h)
        res += 1
        day += 1
        while h and h[0] < day:
            heapq.heappop(h)
    return res

# Example usage:
events = [[1,2],[2,3],[3,4]]
print(maxEvents(events))  # Output: 3
