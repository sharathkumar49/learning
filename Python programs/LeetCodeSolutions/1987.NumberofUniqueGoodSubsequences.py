"""
LeetCode 1987. Number of Unique Good Subsequences

Given a binary string binary, return the number of unique good subsequences modulo 10^9+7.

Example:
Input: binary = "001"
Output: 2

Constraints:
- 1 <= binary.length <= 10^5
- binary consists of '0' and '1'.
"""

MOD = 10**9+7

def numberOfUniqueGoodSubsequences(binary):
    end0 = end1 = has0 = 0
    for c in binary:
        if c == '1':
            end1 = (end0 + end1 + 1) % MOD
        else:
            end0 = (end0 + end1) % MOD
            has0 = 1
    return (end0 + end1 + has0) % MOD

# Example usage:
# print(numberOfUniqueGoodSubsequences("001"))  # Output: 2
