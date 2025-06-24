"""
1223. Dice Roll Simulation

Given an integer n, return the number of distinct sequences of dice rolls of length n such that no number appears more than its rollMax[i] times consecutively. Return the answer modulo 10^9 + 7.

Constraints:
- 1 <= n <= 5000
- rollMax.length == 6
- 1 <= rollMax[i] <= n

Example:
Input: n = 2, rollMax = [1,1,2,2,2,3]
Output: 34

"""
def dieSimulator(n, rollMax):
    MOD = 10**9 + 7
    dp = [[0]*6 for _ in range(n+1)]
    s = [0]*(n+1)
    s[0] = 1
    for i in range(1, n+1):
        for j in range(6):
            dp[i][j] = s[i-1]
            if i - rollMax[j] - 1 >= 0:
                dp[i][j] -= s[i-rollMax[j]-1]
                dp[i][j] += dp[i-rollMax[j]-1][j]
            dp[i][j] %= MOD
        s[i] = sum(dp[i]) % MOD
    return s[n]

# Example usage
if __name__ == "__main__":
    print(dieSimulator(2, [1,1,2,2,2,3]))  # Output: 34
