"""
313. Super Ugly Number

A super ugly number is a positive integer whose prime factors are in the array primes. Given an integer n and an array of integers primes, return the nth super ugly number.

Constraints:
- 1 <= n <= 10^6
- 1 <= primes.length <= 100
- 2 <= primes[i] <= 1000
- primes[i] is guaranteed to be a prime number.
- All the values of primes are unique.
"""
from typing import List
import heapq

class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        ugly = [1]
        idx = [0] * len(primes)
        vals = primes[:]
        for _ in range(1, n):
            next_ugly = min(vals)
            ugly.append(next_ugly)
            for i in range(len(primes)):
                if vals[i] == next_ugly:
                    idx[i] += 1
                    vals[i] = ugly[idx[i]] * primes[i]
        return ugly[-1]

# Example usage:
n = 12
primes = [2,7,13,19]
print(Solution().nthSuperUglyNumber(n, primes))  # Output: 32
