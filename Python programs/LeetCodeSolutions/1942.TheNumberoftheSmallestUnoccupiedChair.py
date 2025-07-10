"""
LeetCode 1942. The Number of the Smallest Unoccupied Chair

Given two arrays times and a targetFriend, return the number of the smallest unoccupied chair the targetFriend will sit on.

Example:
Input: times = [[1,4],[2,3],[4,6]], targetFriend = 1
Output: 1

Constraints:
- n == times.length
- 1 <= n <= 10^4
- 1 <= times[i][0] < times[i][1] <= 10^9
- 0 <= targetFriend < n
"""

def smallestChair(times, targetFriend):
    import heapq
    n = len(times)
    arr = sorted((a, l, i) for i, (a, l) in enumerate(times))
    leave = []
    free = list(range(n))
    heapq.heapify(free)
    for a, l, i in arr:
        while leave and leave[0][0] <= a:
            _, chair = heapq.heappop(leave)
            heapq.heappush(free, chair)
        chair = heapq.heappop(free)
        if i == targetFriend:
            return chair
        heapq.heappush(leave, (l, chair))

# Example usage:
# print(smallestChair([[1,4],[2,3],[4,6]], 1))  # Output: 1
