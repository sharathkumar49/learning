"""
166. Fraction to Recurring Decimal
https://leetcode.com/problems/fraction-to-recurring-decimal/

Given two integers representing the numerator and denominator, return the fraction in string format. If the fractional part is repeating, enclose the repeating part in parentheses.

Constraints:
- -2^31 <= numerator, denominator <= 2^31 - 1
- denominator != 0

Example:
Input: numerator = 1, denominator = 2
Output: "0.5"
"""
def fractionToDecimal(numerator: int, denominator: int) -> str:
    if numerator == 0:
        return "0"
    res = []
    if (numerator < 0) ^ (denominator < 0):
        res.append('-')
    numerator, denominator = abs(numerator), abs(denominator)
    res.append(str(numerator // denominator))
    remainder = numerator % denominator
    if remainder == 0:
        return ''.join(res)
    res.append('.')
    rem_pos = {}
    while remainder:
        if remainder in rem_pos:
            res.insert(rem_pos[remainder], '(')
            res.append(')')
            break
        rem_pos[remainder] = len(res)
        remainder *= 10
        res.append(str(remainder // denominator))
        remainder %= denominator
    return ''.join(res)

# Example usage:
if __name__ == "__main__":
    print(fractionToDecimal(1, 2))    # Output: "0.5"
    print(fractionToDecimal(2, 1))    # Output: "2"
    print(fractionToDecimal(2, 3))    # Output: "0.(6)"
