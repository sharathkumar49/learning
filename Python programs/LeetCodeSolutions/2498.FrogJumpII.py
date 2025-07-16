"""
LeetCode 2498. Frog Jump II

Given stones, return the minimum energy required for the frog to reach the last stone.

Constraints:
- 2 <= stones.length <= 10^5
"""

def maxJump(stones):
    return max(stones[i+1]-stones[i] for i in range(len(stones)-1))

# Example usage:
# print(maxJump([0,2,5,6,7]))  # Output: 3
