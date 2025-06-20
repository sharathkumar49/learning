# 7. Reverse Integer
# Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-2^31, 2^31 - 1], then return 0.
#
# Example 1:
# Input: x = 123
# Output: 321
#
# Example 2:
# Input: x = -123
# Output: -321
#
# Example 3:
# Input: x = 120
# Output: 21
#
# Constraints:
# -2^31 <= x <= 2^31 - 1

def reverse(x):
    sign = -1 if x < 0 else 1
    x_abs = abs(x)
    rev = 0
    while x_abs:
        rev = rev * 10 + x_abs % 10
        x_abs //= 10
    rev *= sign
    if rev < -2**31 or rev > 2**31 - 1:
        return 0
    return rev

# Example usage
x = 123
print("Reversed integer:", reverse(x))  # Output: 321
