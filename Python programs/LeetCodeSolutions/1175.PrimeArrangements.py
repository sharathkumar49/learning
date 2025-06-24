"""
1175. Prime Arrangements

Return the number of valid arrangements of n distinct numbers such that all prime numbers are at prime indices (1-indexed). Return the answer modulo 10^9 + 7.

Constraints:
- 1 <= n <= 100

Example:
Input: n = 5
Output: 12

"""
def numPrimeArrangements(n):
    MOD = 10**9 + 7
    def is_prime(x):
        if x < 2:
            return False
        for i in range(2, int(x**0.5)+1):
            if x % i == 0:
                return False
        return True
    from math import factorial
    primes = sum(is_prime(i) for i in range(1, n+1))
    return (factorial(primes) * factorial(n - primes)) % MOD

# Example usage
if __name__ == "__main__":
    print(numPrimeArrangements(5))  # Output: 12
