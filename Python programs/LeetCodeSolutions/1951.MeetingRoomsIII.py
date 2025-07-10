"""
LeetCode 1951. Meeting Rooms III

Given n rooms and a list of meetings, return the room that held the most meetings.

Example:
Input: n = 2, meetings = [[0,10],[1,5],[2,7],[3,4]]
Output: 0

Constraints:
- 1 <= n <= 100
- 1 <= meetings.length <= 10^5
- 0 <= start < end <= 10^9
"""

def mostBooked(n, meetings):
    import heapq
    rooms = [0]*n
    free = list(range(n))
    heapq.heapify(free)
    busy = []
    meetings.sort()
    for start, end in meetings:
        while busy and busy[0][0] <= start:
            _, room = heapq.heappop(busy)
            heapq.heappush(free, room)
        if free:
            room = heapq.heappop(free)
            rooms[room] += 1
            heapq.heappush(busy, (end, room))
        else:
            t, room = heapq.heappop(busy)
            rooms[room] += 1
            heapq.heappush(busy, (t + end - start, room))
    return rooms.index(max(rooms))

# Example usage:
# print(mostBooked(2, [[0,10],[1,5],[2,7],[3,4]]))  # Output: 0
