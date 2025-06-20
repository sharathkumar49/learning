"""
526. Beautiful Arrangement

Suppose you have n integers from 1 to n. A beautiful arrangement is an array that is constructed by these n numbers satisfying that for the ith position (1 <= i <= n), either the number at the ith position is divisible by i or i is divisible by the number at the ith position.
Return the number of beautiful arrangements that you can construct.

Constraints:
- 1 <= n <= 15

Example:
Input: n = 2
Output: 2
"""

class Solution:
    def countArrangement(self, n: int) -> int:
        def backtrack(pos, used):
            if pos > n:
                return 1
            res = 0
            for i in range(1, n+1):
                if not used[i] and (i % pos == 0 or pos % i == 0):
                    used[i] = True
                    res += backtrack(pos+1, used)
                    used[i] = False
            return res
        used = [False] * (n+1)
        return backtrack(1, used)

# Example usage:
sol = Solution()
print(sol.countArrangement(2))  # Output: 2
