"""
LeetCode 1447. Simplified Fractions

Given an integer n, return a list of all simplified fractions between 0 and 1 (exclusive) with denominators less than or equal to n.

Constraints:
- 1 <= n <= 100

Example:
Input: n = 4
Output: ["1/2","1/3","2/3","1/4","3/4"]
"""
def simplifiedFractions(n):
    from math import gcd
    res = []
    for denom in range(2, n+1):
        for num in range(1, denom):
            if gcd(num, denom) == 1:
                res.append(f"{num}/{denom}")
    return res

# Example usage:
n = 4
print(simplifiedFractions(n))  # Output: ['1/2', '1/3', '2/3', '1/4', '3/4']
