"""
507. Perfect Number

Given a positive integer num, return true if num is a perfect number, otherwise return false. A perfect number is a positive integer that is equal to the sum of its positive divisors, excluding itself.

Constraints:
- 1 <= num <= 10^8

Example:
Input: num = 28
Output: true
"""

class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num <= 1:
            return False
        s = 1
        i = 2
        while i * i <= num:
            if num % i == 0:
                s += i
                if i != num // i:
                    s += num // i
            i += 1
        return s == num

# Example usage:
sol = Solution()
print(sol.checkPerfectNumber(28))  # Output: True
