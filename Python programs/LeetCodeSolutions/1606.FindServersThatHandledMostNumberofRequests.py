"""
LeetCode 1606. Find Servers That Handled Most Number of Requests

You have k servers numbered from 0 to k-1 that handle incoming requests. Each request arrives at arrival[i] and takes load[i] time. Return the list of servers that handled the most number of requests.

Example 1:
Input: k = 3, arrival = [1,2,3,4,5], load = [5,2,3,3,3]
Output: [1]

Constraints:
- 1 <= k <= 10^5
- 1 <= arrival.length, load.length <= 10^5
- arrival.length == load.length
- 1 <= arrival[i], load[i] <= 10^9
"""

def busiestServers(k, arrival, load):
    import heapq
    free = list(range(k))
    busy = []
    count = [0]*k
    for i, (start, l) in enumerate(zip(arrival, load)):
        while busy and busy[0][0] <= start:
            _, server = heapq.heappop(busy)
            heapq.heappush(free, server if server >= i%k else server+k)
        if not free:
            continue
        idx = heapq.heappop(free)%k
        count[idx] += 1
        heapq.heappush(busy, (start+l, idx))
    max_count = max(count)
    return [i for i, c in enumerate(count) if c == max_count]

# Example usage:
# k = 3
# arrival = [1,2,3,4,5]
# load = [5,2,3,3,3]
# print(busiestServers(k, arrival, load))  # Output: [1]
