"""
1155. Number of Dice Rolls With Target Sum

Given n dice each with k faces numbered 1 to k, return the number of possible ways to roll the dice so the sum is target. Since the answer may be large, return it modulo 10^9 + 7.

Constraints:
- 1 <= n, k <= 30
- 1 <= target <= 1000

Example:
Input: n = 1, k = 6, target = 3
Output: 1

"""
def numRollsToTarget(n, k, target):
    MOD = 10**9 + 7
    dp = [0] * (target + 1)
    dp[0] = 1
    for _ in range(n):
        ndp = [0] * (target + 1)
        for t in range(1, target + 1):
            for face in range(1, k + 1):
                if t - face >= 0:
                    ndp[t] = (ndp[t] + dp[t - face]) % MOD
        dp = ndp
    return dp[target]

# Example usage
if __name__ == "__main__":
    print(numRollsToTarget(1, 6, 3))  # Output: 1
