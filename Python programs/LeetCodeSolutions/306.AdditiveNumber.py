"""
306. Additive Number

An additive number is a string whose digits can form an additive sequence. A valid additive sequence should contain at least three numbers. Except for the first two numbers, each subsequent number in the sequence must be the sum of the preceding two.

Given a string containing only digits, return true if it is an additive number, or false otherwise.

Constraints:
- 1 <= num.length <= 35
- num consists only of digits.
- 0 <= num[i] <= 9
- num does not contain leading zeros, except for the number 0 itself.
"""
class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        n = len(num)
        for i in range(1, n):
            for j in range(i+1, n):
                a, b = num[:i], num[i:j]
                if (len(a) > 1 and a[0] == '0') or (len(b) > 1 and b[0] == '0'):
                    continue
                x, y = int(a), int(b)
                k = j
                while k < n:
                    z = x + y
                    z_str = str(z)
                    if not num.startswith(z_str, k):
                        break
                    k += len(z_str)
                    x, y = y, z
                if k == n:
                    return True
        return False

# Example usage:
num = "112358"
print(Solution().isAdditiveNumber(num))  # Output: True
