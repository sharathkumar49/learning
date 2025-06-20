"""
440. K-th Smallest in Lexicographical Order

Given integers n and k, find the k-th smallest integer in the range [1, n] when ordered lexicographically.

Constraints:
- 1 <= k <= n <= 10^9

Example:
Input: n = 13, k = 2
Output: 10
"""

class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        def calcSteps(n, curr, next):
            steps = 0
            while curr <= n:
                steps += min(n+1, next) - curr
                curr *= 10
                next *= 10
            return steps
        curr = 1
        k -= 1
        while k > 0:
            steps = calcSteps(n, curr, curr+1)
            if steps <= k:
                curr += 1
                k -= steps
            else:
                curr *= 10
                k -= 1
        return curr

# Example usage:
sol = Solution()
print(sol.findKthNumber(13, 2))  # Output: 10
