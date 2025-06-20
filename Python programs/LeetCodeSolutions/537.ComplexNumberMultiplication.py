"""
537. Complex Number Multiplication

Given two strings representing two complex numbers, return a string representing their multiplication.

Constraints:
- Both input strings are valid complex numbers.

Example:
Input: num1 = "1+1i", num2 = "1+1i"
Output: "0+2i"
"""

class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        a, b = map(int, num1[:-1].split('+'))
        c, d = map(int, num2[:-1].split('+'))
        real = a * c - b * d
        imag = a * d + b * c
        return f"{real}+{imag}i"

# Example usage:
sol = Solution()
print(sol.complexNumberMultiply("1+1i", "1+1i"))  # Output: "0+2i"
