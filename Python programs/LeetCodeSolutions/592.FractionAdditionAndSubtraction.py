"""
592. Fraction Addition and Subtraction
Difficulty: Medium

Given a string expression representing an expression of fraction addition and subtraction, return the calculation result in string format. The final result should be an irreducible fraction.

Example 1:
Input: expression = "-1/2+1/2"
Output: "0/1"

Example 2:
Input: expression = "-1/2+1/2+1/3"
Output: "1/3"

Constraints:
The input string only contains '0'-'9', '+', '-', and '/'.
"""

def fractionAddition(expression: str) -> str:
    import re
    from math import gcd
    nums = re.findall('[+-]?\d+/\d+', expression)
    numerator, denominator = 0, 1
    for frac in nums:
        n, d = map(int, frac.split('/'))
        numerator = numerator * d + n * denominator
        denominator *= d
        g = gcd(abs(numerator), abs(denominator))
        numerator //= g
        denominator //= g
    return f"{numerator}/{denominator}"

# Example usage
if __name__ == "__main__":
    print(fractionAddition("-1/2+1/2"))      # Output: "0/1"
    print(fractionAddition("-1/2+1/2+1/3"))  # Output: "1/3"
