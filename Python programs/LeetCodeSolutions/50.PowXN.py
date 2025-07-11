# 50. Pow(x, n)
# Implement pow(x, n), which calculates x raised to the power n (i.e., x^n).
#
# Example 1:
# Input: x = 2.00000, n = 10
# Output: 1024.00000
#
# Example 2:
# Input: x = 2.10000, n = 3
# Output: 9.26100
#
# Example 3:
# Input: x = 2.00000, n = -2
# Output: 0.25000
#
# Constraints:
# -100.0 < x < 100.0
# -2^31 <= n <= 2^31-1
# -10^4 <= x^n <= 10^4

def myPow(x, n):
    if n == 0:
        return 1
    if n < 0:
        x = 1 / x
        n = -n
    res = 1
    while n:
        if n % 2:
            res *= x
        x *= x
        n //= 2
    return res

# Example usage
x = 2.0
n = 10
print("Pow(x, n):", myPow(x, n))  # Output: 1024.0
