"""
1201. Ugly Number III

Given three positive integers a, b, c, return the nth ugly number that is divisible by a, b, or c.

Constraints:
- 1 <= n, a, b, c <= 10^9
- 1 <= a * b * c <= 10^{18}

Example:
Input: n = 3, a = 2, b = 3, c = 5
Output: 4

"""
def nthUglyNumber(n, a, b, c):
    from math import gcd
    def lcm(x, y):
        return x * y // gcd(x, y)
    def count(x):
        ab = lcm(a, b)
        ac = lcm(a, c)
        bc = lcm(b, c)
        abc = lcm(ab, c)
        return x//a + x//b + x//c - x//ab - x//ac - x//bc + x//abc
    left, right = 1, 2*10**18
    while left < right:
        mid = (left + right) // 2
        if count(mid) < n:
            left = mid + 1
        else:
            right = mid
    return left

# Example usage
if __name__ == "__main__":
    print(nthUglyNumber(3, 2, 3, 5))  # Output: 4
