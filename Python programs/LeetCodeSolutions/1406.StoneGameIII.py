"""
LeetCode 1406. Stone Game III

Alice and Bob take turns playing a game with a row of stones. Each stone has a value. On each player's turn, they can take 1, 2, or 3 stones from the row. The player with the largest total value wins. Return "Alice" if Alice wins, "Bob" if Bob wins, or "Tie" if the game ends with a tie.

Constraints:
- 1 <= stoneValue.length <= 5 * 10^4
- -1000 <= stoneValue[i] <= 1000

Example:
Input: stoneValue = [1,2,3,7]
Output: "Bob"
"""
def stoneGameIII(stoneValue):
    n = len(stoneValue)
    dp = [0] * (n+1)
    for i in range(n-1, -1, -1):
        dp[i] = stoneValue[i] - dp[i+1]
        if i+1 < n:
            dp[i] = max(dp[i], stoneValue[i]+stoneValue[i+1]-dp[i+2])
        if i+2 < n:
            dp[i] = max(dp[i], stoneValue[i]+stoneValue[i+1]+stoneValue[i+2]-dp[i+3])
    if dp[0] > 0:
        return "Alice"
    elif dp[0] < 0:
        return "Bob"
    else:
        return "Tie"

# Example usage:
stoneValue = [1,2,3,7]
print(stoneGameIII(stoneValue))  # Output: "Bob"
