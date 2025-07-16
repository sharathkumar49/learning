"""
LeetCode 2281. Sum of Total Strength of Wizards

Given strength, return the sum of total strength of all wizards.

Example:
Input: strength = [1,3,1,2]
Output: 44

Constraints:
- 1 <= strength.length <= 10^5
- 1 <= strength[i] <= 10^9
"""

def totalStrength(strength):
    MOD = 10**9+7
    n = len(strength)
    res = 0
    for i in range(n):
        min_val = strength[i]
        for j in range(i, n):
            min_val = min(min_val, strength[j])
            res = (res + min_val * sum(strength[i:j+1])) % MOD
    return res

# Example usage:
# print(totalStrength([1,3,1,2]))  # Output: 44
