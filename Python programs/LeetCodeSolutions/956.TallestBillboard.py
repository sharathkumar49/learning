"""
956. Tallest Billboard
https://leetcode.com/problems/tallest-billboard/

You are given an array rods where rods[i] represents the length of the ith rod. You want to build two billboards of the same height by welding together some rods. Return the maximum possible height of the two billboards that can be built, or 0 if it is impossible.

Constraints:
- 1 <= rods.length <= 20
- 1 <= rods[i] <= 1000
- sum(rods[i]) <= 5000

Example:
Input: rods = [1,2,3,6]
Output: 6
"""
from typing import List

class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:
        dp = {0: 0}
        for rod in rods:
            cur = dp.copy()
            for diff, y in cur.items():
                dp[diff + rod] = max(dp.get(diff + rod, 0), y)
                dp[abs(diff - rod)] = max(dp.get(abs(diff - rod), 0), y + min(diff, rod))
        return dp[0]

# Example usage
if __name__ == "__main__":
    rods = [1,2,3,6]
    print(Solution().tallestBillboard(rods))  # Output: 6
