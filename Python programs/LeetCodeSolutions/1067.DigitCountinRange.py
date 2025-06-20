"""
1067. Digit Count in Range

Given two integers d and n, return the number of times digit d occurs in all numbers from 1 to n.

Constraints:
- 0 <= d <= 9
- 1 <= n <= 10^8

Example:
Input: d = 1, n = 13
Output: 6
"""
def digitsCount(d: int, n: int) -> int:
    def count(n):
        if n == 0:
            return 0
        res, k = 0, 1
        while k <= n:
            high = n // (k * 10)
            cur = (n // k) % 10
            low = n % k
            if d == 0:
                if high:
                    res += (high - 1) * k + (cur > 0) * k + (cur == 0) * (low + 1)
            else:
                res += high * k + (cur > d) * k + (cur == d) * (low + 1)
            k *= 10
        return res
    return count(n) if d else count(n) - count(0)

# Example usage:
d = 1
n = 13
print(digitsCount(d, n))  # Output: 6
