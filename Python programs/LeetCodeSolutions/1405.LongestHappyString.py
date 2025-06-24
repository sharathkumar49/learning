"""
LeetCode 1405. Longest Happy String

Given three integers a, b, and c, return the longest possible string that can be formed under the following rules:
- The string consists of only 'a', 'b', and 'c'.
- The string cannot contain "aaa", "bbb", or "ccc" as a substring.
- a, b, c are the maximum number of times 'a', 'b', and 'c' can be used respectively.

Constraints:
- 0 <= a, b, c <= 100
- a + b + c > 0

Example:
Input: a = 1, b = 1, c = 7
Output: "ccaccbcc"
"""
def longestDiverseString(a, b, c):
    res = []
    pq = []
    for count, char in [(-a, 'a'), (-b, 'b'), (-c, 'c')]:
        if count != 0:
            import heapq
            heapq.heappush(pq, (count, char))
    while pq:
        count1, char1 = heapq.heappop(pq)
        if len(res) >= 2 and res[-1] == res[-2] == char1:
            if not pq:
                break
            count2, char2 = heapq.heappop(pq)
            res.append(char2)
            count2 += 1
            if count2 != 0:
                heapq.heappush(pq, (count2, char2))
            heapq.heappush(pq, (count1, char1))
        else:
            res.append(char1)
            count1 += 1
            if count1 != 0:
                heapq.heappush(pq, (count1, char1))
    return ''.join(res)

# Example usage:
a, b, c = 1, 1, 7
print(longestDiverseString(a, b, c))  # Output: "ccaccbcc"
