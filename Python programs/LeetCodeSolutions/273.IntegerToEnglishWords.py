"""
273. Integer to English Words
https://leetcode.com/problems/integer-to-english-words/

Convert a non-negative integer num to its English words representation.

Constraints:
- 0 <= num <= 2^31 - 1

Example 1:
Input: num = 123
Output: "One Hundred Twenty Three"

Example 2:
Input: num = 12345
Output: "Twelve Thousand Three Hundred Forty Five"

Example 3:
Input: num = 1234567
Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
"""
def numberToWords(num):
    if num == 0:
        return "Zero"
    below_20 = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
    tens = ["", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
    thousands = ["", "Thousand", "Million", "Billion"]
    def helper(n):
        if n == 0:
            return ""
        elif n < 20:
            return below_20[n] + " "
        elif n < 100:
            return tens[n // 10] + " " + helper(n % 10)
        else:
            return below_20[n // 100] + " Hundred " + helper(n % 100)
    res = ""
    for i, unit in enumerate(thousands):
        if num % 1000 != 0:
            res = helper(num % 1000) + unit + " " + res
        num //= 1000
    return res.strip()

# Example usage:
if __name__ == "__main__":
    print(numberToWords(123))        # Output: "One Hundred Twenty Three"
    print(numberToWords(12345))      # Output: "Twelve Thousand Three Hundred Forty Five"
    print(numberToWords(1234567))    # Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
