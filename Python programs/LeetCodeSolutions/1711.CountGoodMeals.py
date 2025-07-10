"""
LeetCode 1711. Count Good Meals

You are given an integer array deliciousness. A good meal is a pair of different indices (i, j) such that deliciousness[i] + deliciousness[j] is a power of two. Return the number of good meals modulo 10^9 + 7.

Example 1:
Input: deliciousness = [1,3,5,7,9]
Output: 4

Constraints:
- 1 <= deliciousness.length <= 10^5
- 0 <= deliciousness[i] <= 2^20
"""

def countPairs(deliciousness):
    from collections import Counter
    MOD = 10**9 + 7
    count = Counter()
    res = 0
    for x in deliciousness:
        for p in range(22):
            res += count[(1 << p) - x]
        count[x] += 1
    return res % MOD

# Example usage:
# deliciousness = [1,3,5,7,9]
# print(countPairs(deliciousness))  # Output: 4
