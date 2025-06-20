"""
204. Count Primes
https://leetcode.com/problems/count-primes/

Count the number of prime numbers less than a non-negative number, n.

Constraints:
- 0 <= n <= 5 * 10^6

Example 1:
Input: n = 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.

Example 2:
Input: n = 0
Output: 0

Example 3:
Input: n = 1
Output: 0
"""
def countPrimes(n):
    if n < 2:
        return 0
    is_prime = [True] * n
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i*i, n, i):
                is_prime[j] = False
    return sum(is_prime)

# Example usage:
if __name__ == "__main__":
    print(countPrimes(10))  # Output: 4
    print(countPrimes(0))   # Output: 0
    print(countPrimes(1))   # Output: 0
