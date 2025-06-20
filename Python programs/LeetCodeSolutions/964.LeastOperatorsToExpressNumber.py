"""
964. Least Operators to Express Number
https://leetcode.com/problems/least-operators-to-express-number/

Given a single integer x and a target, return the least number of operators to express the target number using only x, +, -, *, and /, and parentheses. You may use any number of x's. Division is integer division.

Constraints:
- 2 <= x <= 100
- 1 <= target <= 2 * 10^8

Example:
Input: x = 3, target = 19
Output: 5
"""
class Solution:
    def leastOpsExpressTarget(self, x: int, target: int) -> int:
        from functools import lru_cache
        @lru_cache(None)
        def dp(t):
            if t == 0: return 0
            if t < x: return min(t*2-1, (x-t)*2)
            k = 0
            p = 1
            while p * x <= t:
                p *= x
                k += 1
            res = dp(t - p//x) + k
            if p - t < t:
                res = min(res, dp(p-t) + k + 1)
            return res
        return dp(target)

# Example usage
if __name__ == "__main__":
    x = 3
    target = 19
    print(Solution().leastOpsExpressTarget(x, target))  # Output: 5
