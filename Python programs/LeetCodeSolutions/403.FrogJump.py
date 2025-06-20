"""
403. Frog Jump

A frog is crossing a river. The river is divided into some number of units, and at each unit, there may or may not exist a stone. The frog can jump on a stone, but it must not jump into the water.

Given a list of stones' positions (in units) in sorted ascending order, determine if the frog can cross the river by landing on the last stone.

Constraints:
- 2 <= stones.length <= 2000
- 0 <= stones[i] <= 2^31 - 1
- stones[0] == 0
- stones[1] == 1
- stones[i] > stones[i - 1] for 1 <= i < stones.length
"""
from typing import List

class Solution:
    def canCross(self, stones: List[int]) -> bool:
        stone_set = set(stones)
        last = stones[-1]
        memo = {}
        def dfs(pos, jump):
            if (pos, jump) in memo:
                return memo[(pos, jump)]
            if pos == last:
                return True
            for k in [jump-1, jump, jump+1]:
                if k > 0 and (pos + k) in stone_set:
                    if dfs(pos + k, k):
                        memo[(pos, jump)] = True
                        return True
            memo[(pos, jump)] = False
            return False
        return dfs(0, 0)

# Example usage:
stones = [0,1,3,5,6,8,12,17]
print(Solution().canCross(stones))  # Output: True
