"""
LeetCode 2266. Count Number of Texts

Given pressedKeys, return the number of possible text messages.

Example:
Input: pressedKeys = "22233"
Output: 8

Constraints:
- 1 <= pressedKeys.length <= 10^5
"""

def countTexts(pressedKeys):
    MOD = 10**9+7
    n = len(pressedKeys)
    dp = [1]+[0]*n
    for i in range(1, n+1):
        for k in range(1, 5 if pressedKeys[i-1] in '79' else 4):
            if i-k >= 0 and all(pressedKeys[i-1] == pressedKeys[i-j-1] for j in range(k)):
                dp[i] = (dp[i] + dp[i-k]) % MOD
    return dp[n]

# Example usage:
# print(countTexts("22233"))  # Output: 8
