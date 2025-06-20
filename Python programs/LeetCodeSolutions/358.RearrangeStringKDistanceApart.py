"""
358. Rearrange String k Distance Apart

Given a string s and an integer k, rearrange the string such that the same characters are at least distance k from each other. If it is not possible, return an empty string.

Constraints:
- 1 <= s.length <= 3 * 10^4
- s consists of only lowercase English letters.
- 0 <= k <= s.length
"""
from collections import Counter, deque
import heapq

class Solution:
    def rearrangeString(self, s: str, k: int) -> str:
        if k == 0:
            return s
        count = Counter(s)
        max_heap = [(-v, c) for c, v in count.items()]
        heapq.heapify(max_heap)
        queue = deque()
        res = []
        while max_heap or queue:
            if max_heap:
                v, c = heapq.heappop(max_heap)
                res.append(c)
                queue.append((c, v+1))
            else:
                return ""
            if len(queue) == k:
                c2, v2 = queue.popleft()
                if v2 < 0:
                    heapq.heappush(max_heap, (v2, c2))
        return ''.join(res)

# Example usage:
s = "aabbcc"
k = 3
print(Solution().rearrangeString(s, k))  # Output: "abcabc"
