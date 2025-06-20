"""
405. Convert a Number to Hexadecimal

Given an integer num, return its hexadecimal representation as a string. All the letters in the answer should be lowercase, and there should not be any leading zeros except for the zero itself.

Constraints:
- -2^31 <= num <= 2^31 - 1
"""
class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return "0"
        hex_chars = "0123456789abcdef"
        res = ""
        num &= 0xFFFFFFFF
        while num:
            res = hex_chars[num & 0xF] + res
            num >>= 4
        return res

# Example usage:
num = 26
print(Solution().toHex(num))  # Output: "1a"
