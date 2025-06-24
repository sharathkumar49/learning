"""
1230. Toss Strange Coins

Given n coins with probabilities of heads, return the probability of getting exactly target heads.

Constraints:
- 1 <= n <= 1000
- 0 <= prob[i] <= 1
- 0 <= target <= n

Example:
Input: prob = [0.4], target = 1
Output: 0.4

"""
def probabilityOfHeads(prob, target):
    n = len(prob)
    dp = [0.0] * (target + 1)
    dp[0] = 1.0
    for p in prob:
        for k in range(target, -1, -1):
            dp[k] = dp[k] * (1 - p) + (dp[k-1] * p if k > 0 else 0)
    return dp[target]

# Example usage
if __name__ == "__main__":
    print(probabilityOfHeads([0.4], 1))  # Output: 0.4
