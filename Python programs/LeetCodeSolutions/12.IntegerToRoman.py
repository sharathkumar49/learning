# 12. Integer to Roman
# Given an integer, convert it to a roman numeral.
#
# Example 1:
# Input: num = 3
# Output: "III"
#
# Example 2:
# Input: num = 58
# Output: "LVIII"
#
# Example 3:
# Input: num = 1994
# Output: "MCMXCIV"
#
# Constraints:
# 1 <= num <= 3999

def intToRoman(num):
    val = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    syb = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    roman = ''
    for i in range(len(val)):
        while num >= val[i]:
            roman += syb[i]
            num -= val[i]
    return roman

# Example usage
num = 1994
print("Integer to Roman:", intToRoman(num))  # Output: "MCMXCIV"
