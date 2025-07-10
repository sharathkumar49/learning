"""
LeetCode 2117. Abbreviating the Product of a Range

Given left and right, return the abbreviation of the product of all integers in the range [left, right].

Example:
Input: left = 1, right = 4
Output: "24"

Constraints:
- 1 <= left <= right <= 10^12
- right - left <= 4 * 10^4
"""

def abbreviateProduct(left, right):
    import math
    prod = 1
    zero = 0
    for i in range(left, right+1):
        prod *= i
        while prod % 10 == 0:
            prod //= 10
            zero += 1
        prod %= 10**12
    s = str(prod)
    if len(s) > 10:
        return s[:5] + '...' + s[-5:] + 'e' + str(zero)
    else:
        return s + 'e' + str(zero)

# Example usage:
# print(abbreviateProduct(1, 4))  # Output: "24"
