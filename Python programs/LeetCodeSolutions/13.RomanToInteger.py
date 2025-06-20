# 13. Roman to Integer
# Given a roman numeral, convert it to an integer.
#
# Example 1:
# Input: s = "III"
# Output: 3
#
# Example 2:
# Input: s = "IV"
# Output: 4
#
# Example 3:
# Input: s = "IX"
# Output: 9
#
# Example 4:
# Input: s = "LVIII"
# Output: 58
#
# Example 5:
# Input: s = "MCMXCIV"
# Output: 1994
#
# Constraints:
# 1 <= s.length <= 15
# s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').

def romanToInt(s):
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0
    prev = 0
    for c in reversed(s):
        if roman[c] < prev:
            total -= roman[c]
        else:
            total += roman[c]
        prev = roman[c]
    return total

# Example usage
s = "MCMXCIV"
print("Roman to Integer:", romanToInt(s))  # Output: 1994
