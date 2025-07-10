"""
LeetCode 1705. Maximum Number of Eaten Apples

There is an apple tree that grows apples every day. On the ith day, you are given apples[i] apples, and each apple expires in days[i] days. You can eat at most one apple per day. Return the maximum number of apples you can eat.

Example 1:
Input: apples = [1,2,3,5,2], days = [3,2,1,4,2]
Output: 7

Constraints:
- 1 <= apples.length, days.length <= 2 * 10^4
- 0 <= apples[i], days[i] <= 2 * 10^4
"""
import heapq

def eatenApples(apples, days):
    import heapq
    n = len(apples)
    heap = []
    day = 0
    res = 0
    while day < n or heap:
        if day < n and apples[day] > 0:
            heapq.heappush(heap, (day + days[day], apples[day]))
        while heap and heap[0][0] <= day:
            heapq.heappop(heap)
        if heap:
            expire, count = heapq.heappop(heap)
            if count > 1:
                heapq.heappush(heap, (expire, count - 1))
            res += 1
        day += 1
    return res

# Example usage:
# apples = [1,2,3,5,2]
# days = [3,2,1,4,2]
# print(eatenApples(apples, days))  # Output: 7
