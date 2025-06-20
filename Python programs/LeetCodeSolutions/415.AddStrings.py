"""
415. Add Strings

Given two non-negative integers num1 and num2 represented as string, return the sum as a string.

Constraints:
- 1 <= num1.length, num2.length <= 10^4
- num1 and num2 consist of only digits.
- num1 and num2 do not contain any leading zeros except for the zero itself.
"""
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        i, j, carry = len(num1) - 1, len(num2) - 1, 0
        res = []
        while i >= 0 or j >= 0 or carry:
            n1 = int(num1[i]) if i >= 0 else 0
            n2 = int(num2[j]) if j >= 0 else 0
            total = n1 + n2 + carry
            res.append(str(total % 10))
            carry = total // 10
            i -= 1
            j -= 1
        return ''.join(res[::-1])

# Example usage:
num1 = "11"
num2 = "123"
print(Solution().addStrings(num1, num2))  # Output: "134"
