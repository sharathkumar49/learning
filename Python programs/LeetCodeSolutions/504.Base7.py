"""
504. Base 7

Given an integer num, return its base 7 string representation.

Constraints:
- -10^7 <= num <= 10^7

Example:
Input: num = 100
Output: "202"
"""

class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return "0"
        neg = num < 0
        num = abs(num)
        res = ''
        while num:
            res = str(num % 7) + res
            num //= 7
        return '-' + res if neg else res

# Example usage:
sol = Solution()
print(sol.convertToBase7(100))  # Output: "202"
