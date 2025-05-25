# Microsoft: Meeting Rooms II (Minimum Number of Meeting Rooms)
# Given an array of meeting time intervals, find the minimum number of conference rooms required.
import heapq

def min_meeting_rooms(intervals):
    if not intervals:
        return 0
    intervals.sort(key=lambda x: x[0])
    heap = []
    heapq.heappush(heap, intervals[0][1])
    for i in range(1, len(intervals)):
        if intervals[i][0] >= heap[0]:
            heapq.heappop(heap)
        heapq.heappush(heap, intervals[i][1])
    return len(heap)

if __name__ == "__main__":
    intervals1 = [[0,30],[5,10],[15,20]]
    print(min_meeting_rooms(intervals1))  # Output: 2
    intervals2 = [[7,10],[2,4]]
    print(min_meeting_rooms(intervals2))  # Output: 1
