"""
LeetCode 1756. Design Most Recently Used Queue

Design a queue with n elements. Implement fetch(k) to move the kth element to the front and return it.

Example 1:
Input: n = 8, queries = [fetch(3), fetch(5), fetch(2), fetch(8)]
Output: [3,6,2,8]

Constraints:
- 1 <= n <= 2000
- 1 <= k <= n
- At most 2000 calls to fetch
"""
class MRUQueue:
    def __init__(self, n):
        self.q = list(range(1, n+1))
    def fetch(self, k):
        x = self.q.pop(k-1)
        self.q.append(x)
        return x

# Example usage:
# mru = MRUQueue(8)
# print(mru.fetch(3))  # Output: 3
# print(mru.fetch(5))  # Output: 6
# print(mru.fetch(2))  # Output: 2
# print(mru.fetch(8))  # Output: 8
