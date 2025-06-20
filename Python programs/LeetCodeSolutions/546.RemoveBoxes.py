"""
546. Remove Boxes

Given several boxes with different colors represented by different positive numbers, you may remove boxes of the same color that are adjacent, earning points as described in the problem. Return the maximum points you can earn.

Constraints:
- 1 <= boxes.length <= 100
- 1 <= boxes[i] <= 100

Example:
Input: boxes = [1,3,2,2,2,3,4,3,1]
Output: 23
"""

class Solution:
    def removeBoxes(self, boxes: list) -> int:
        from functools import lru_cache
        n = len(boxes)
        @lru_cache(None)
        def dp(l, r, k):
            if l > r:
                return 0
            while l < r and boxes[r] == boxes[r-1]:
                r -= 1
                k += 1
            res = dp(l, r-1, 0) + (k+1)*(k+1)
            for i in range(l, r):
                if boxes[i] == boxes[r]:
                    res = max(res, dp(l, i, k+1) + dp(i+1, r-1, 0))
            return res
        return dp(0, n-1, 0)

# Example usage:
sol = Solution()
print(sol.removeBoxes([1,3,2,2,2,3,4,3,1]))  # Output: 23
