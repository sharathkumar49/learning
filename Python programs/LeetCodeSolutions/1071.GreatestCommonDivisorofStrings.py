"""
1071. Greatest Common Divisor of Strings

Given two strings str1 and str2, return the largest string X such that X divides both str1 and str2 (i.e., both are made by repeating X some number of times).

Constraints:
- 1 <= str1.length, str2.length <= 1000
- str1 and str2 consist of English uppercase letters.

Example:
Input: str1 = "ABCABC", str2 = "ABC"
Output: "ABC"
"""
def gcdOfStrings(str1: str, str2: str) -> str:
    if str1 + str2 != str2 + str1:
        return ""
    from math import gcd
    return str1[:gcd(len(str1), len(str2))]

# Example usage:
str1 = "ABCABC"
str2 = "ABC"
print(gcdOfStrings(str1, str2))  # Output: "ABC"
