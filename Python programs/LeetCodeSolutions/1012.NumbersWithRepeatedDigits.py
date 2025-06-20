"""
1012. Numbers With Repeated Digits

Given a positive integer n, return the number of positive integers in the range [1, n] that have at least one repeated digit.

Constraints:
- 1 <= n <= 10^9

Example:
Input: n = 20
Output: 1
Explanation: Only 11 has repeated digits.
"""
def numDupDigitsAtMostN(n: int) -> int:
    def count_unique(n):
        digits = list(map(int, str(n + 1)))
        res, k = 0, len(digits)
        for i in range(1, k):
            res += 9 * perm(9, i - 1)
        seen = set()
        for i, x in enumerate(digits):
            for y in range(0 if i else 1, x):
                if y not in seen:
                    res += perm(9 - i, k - i - 1)
            if x in seen:
                break
            seen.add(x)
        return res
    def perm(a, b):
        res = 1
        for i in range(b):
            res *= a - i
        return res
    return n - count_unique(n)

# Example usage:
n = 20
print(numDupDigitsAtMostN(n))  # Output: 1
