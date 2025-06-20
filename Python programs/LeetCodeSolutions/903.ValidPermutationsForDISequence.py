"""
903. Valid Permutations for DI Sequence
https://leetcode.com/problems/valid-permutations-for-di-sequence/

You are given a string s of length n where s[i] is either 'D' (decreasing) or 'I' (increasing). A valid permutation perm of [0, 1, ..., n] is a permutation such that for all i:
- If s[i] == 'D', then perm[i] > perm[i+1], and
- If s[i] == 'I', then perm[i] < perm[i+1].
Return the number of valid permutations perm. Since the answer may be large, return it modulo 10^9 + 7.

Constraints:
- 1 <= s.length <= 200
- s[i] is either 'I' or 'D'.

Example:
Input: s = "DID"
Output: 5
"""
class Solution:
    def numPermsDISequence(self, s: str) -> int:
        n = len(s)
        MOD = 10**9 + 7
        dp = [1] * (n+1)
        for i in range(1, n+1):
            ndp = [0] * (n+1)
            if s[i-1] == 'I':
                curr = 0
                for j in range(i):
                    curr = (curr + dp[j]) % MOD
                    ndp[j] = curr
            else:
                curr = 0
                for j in range(i-1, -1, -1):
                    curr = (curr + dp[j+1]) % MOD
                    ndp[j] = curr
            dp = ndp
        return dp[0] % MOD

# Example usage
if __name__ == "__main__":
    s = "DID"
    print(Solution().numPermsDISequence(s))  # Output: 5
