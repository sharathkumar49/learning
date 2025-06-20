"""
502. IPO

Suppose LeetCode will start its IPO soon. In order to sell a good price of its shares to Venture Capital, LeetCode would like to work on some projects to increase its capital before the IPO. Return the maximized capital after at most k projects.

Constraints:
- 1 <= k <= 10^5
- 0 <= w <= 10^9
- n == profits.length == capital.length
- 1 <= n <= 10^5
- 0 <= profits[i], capital[i] <= 10^9

Example:
Input: k = 2, w = 0, profits = [1,2,3], capital = [0,1,1]
Output: 4
"""

import heapq

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: list, capital: list) -> int:
        projects = sorted(zip(capital, profits))
        heap = []
        i = 0
        n = len(profits)
        for _ in range(k):
            while i < n and projects[i][0] <= w:
                heapq.heappush(heap, -projects[i][1])
                i += 1
            if not heap:
                break
            w -= heapq.heappop(heap)
        return w

# Example usage:
sol = Solution()
k = 2
w = 0
profits = [1,2,3]
capital = [0,1,1]
print(sol.findMaximizedCapital(k, w, profits, capital))  # Output: 4
