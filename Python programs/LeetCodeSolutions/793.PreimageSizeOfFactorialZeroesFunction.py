"""
793. Preimage Size of Factorial Zeroes Function

Let f(x) be the number of trailing zeroes in x!. Given k, return the number of non-negative integers x such that f(x) = k.

Example 1:
Input: k = 0
Output: 5

Example 2:
Input: k = 5
Output: 0

Constraints:
- 0 <= k <= 10^9
"""
def preimageSizeFZF(k):
    def zeta(n):
        res = 0
        while n:
            n //= 5
            res += n
        return res
    def left_bound(k):
        lo, hi = 0, 5 * k + 1
        while lo < hi:
            mid = (lo + hi) // 2
            if zeta(mid) < k:
                lo = mid + 1
            else:
                hi = mid
        return lo
    return left_bound(k+1) - left_bound(k)

# Example usage:
print(preimageSizeFZF(0))  # Output: 5
print(preimageSizeFZF(5))  # Output: 0
