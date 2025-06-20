# 29. Divide Two Integers
# Given two integers dividend and divisor, divide two integers without using multiplication, division, and mod operator.
# Return the quotient after dividing dividend by divisor.
#
# Example 1:
# Input: dividend = 10, divisor = 3
# Output: 3
#
# Example 2:
# Input: dividend = 7, divisor = -3
# Output: -2
#
# Constraints:
# -2^31 <= dividend, divisor <= 2^31 - 1
# divisor != 0
# It is guaranteed that the result will be in the range [-2^31, 2^31 - 1].

def divide(dividend, divisor):
    INT_MAX = 2**31 - 1
    INT_MIN = -2**31
    if dividend == INT_MIN and divisor == -1:
        return INT_MAX
    sign = (dividend > 0) == (divisor > 0)
    dvd, dvs = abs(dividend), abs(divisor)
    res = 0
    while dvd >= dvs:
        temp, multiple = dvs, 1
        while dvd >= (temp << 1):
            temp <<= 1
            multiple <<= 1
        dvd -= temp
        res += multiple
    return res if sign else -res

# Example usage
dividend = 10
divisor = 3
print("Quotient:", divide(dividend, divisor))  # Output: 3
