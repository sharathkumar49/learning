"""
LeetCode 2218. Maximum Value of K Coins From Piles

Given piles and k, return the maximum value of coins you can get.

Example:
Input: piles = [[1,100,3],[7,8,9]], k = 2
Output: 101

Constraints:
- 1 <= piles.length <= 100
- 1 <= piles[i].length <= 100
- 1 <= k <= sum(len(pile) for pile in piles)
"""

def maxValueOfCoins(piles, k):
    dp = [0]*(k+1)
    for pile in piles:
        for coins in range(k, 0, -1):
            curr = 0
            for i in range(min(len(pile), coins)):
                curr += pile[i]
                dp[coins] = max(dp[coins], dp[coins-i-1]+curr)
    return dp[k]

# Example usage:
# print(maxValueOfCoins([[1,100,3],[7,8,9]], 2))  # Output: 101
