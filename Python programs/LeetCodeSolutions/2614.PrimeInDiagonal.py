"""
LeetCode 2614. Prime In Diagonal

Given a matrix, return the largest prime in the diagonals.

Constraints:
- 1 <= n <= 100
"""

def diagonalPrime(nums):
    def is_prime(x):
        if x < 2: return False
        for i in range(2, int(x**0.5)+1):
            if x % i == 0:
                return False
        return True
    n = len(nums)
    res = 0
    for i in range(n):
        for x in [nums[i][i], nums[i][n-1-i]]:
            if is_prime(x):
                res = max(res, x)
    return res
# Example usage:
# print(diagonalPrime([[1,2,3],[5,6,7],[9,10,11]]))  # Output: 11
