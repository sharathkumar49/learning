"""
LeetCode 1411. Number of Ways to Paint N × 3 Grid

Given the number n, return the number of ways you can paint an n x 3 grid such that no two adjacent cells have the same color. Colors are 3: red, yellow, green. Return the answer modulo 10^9 + 7.

Constraints:
- 1 <= n <= 5000

Example:
Input: n = 1
Output: 12
"""
def numOfWays(n):
    MOD = 10**9+7
    a, b = 6, 6
    for _ in range(1, n):
        a, b = (3*a+2*b)%MOD, (2*a+2*b)%MOD
    return (a+b)%MOD

# Example usage:
n = 1
print(numOfWays(n))  # Output: 12
