"""
483. Smallest Good Base

Given an integer n represented as a string, return the smallest good base of n.
A good base k is such that n = 1 + k + k^2 + ... + k^m for some m >= 1.

Constraints:
- n is an integer in the range [3, 10^18].

Example:
Input: n = "13"
Output: "3"
"""

class Solution:
    def smallestGoodBase(self, n: str) -> str:
        n = int(n)
        max_m = n.bit_length()
        for m in range(max_m, 1, -1):
            k = int(n ** (1/(m-1)))
            if k > 1 and (k**m - 1) // (k - 1) == n:
                return str(k)
        return str(n-1)

# Example usage:
sol = Solution()
print(sol.smallestGoodBase("13"))  # Output: "3"
