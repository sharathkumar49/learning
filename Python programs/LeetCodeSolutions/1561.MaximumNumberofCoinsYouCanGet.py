"""
LeetCode 1561. Maximum Number of Coins You Can Get

Given an array piles, return the maximum number of coins you can get by picking coins as described in the problem statement.

Constraints:
- 3 <= piles.length <= 10^5
- piles.length % 3 == 0
- 1 <= piles[i] <= 10^4

Example:
Input: piles = [2,4,1,2,7,8]
Output: 9
"""
def maxCoins(piles):
    piles.sort()
    n = len(piles) // 3
    return sum(piles[-2*n::2])

# Example usage:
piles = [2,4,1,2,7,8]
print(maxCoins(piles))  # Output: 9
