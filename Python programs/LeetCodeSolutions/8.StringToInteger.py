# 8. String to Integer (atoi)
# Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer (similar to C/C++'s atoi function).
#
# Example 1:
# Input: s = "42"
# Output: 42
#
# Example 2:
# Input: s = "   -42"
# Output: -42
#
# Example 3:
# Input: s = "4193 with words"
# Output: 4193
#
# Constraints:
# 0 <= s.length <= 200
# s consists of English letters (lower-case and upper-case), digits, ' ', '+', '-', and '.'.

def myAtoi(s):
    s = s.lstrip()
    if not s:
        return 0
    sign = 1
    i = 0
    if s[0] in ['-','+']:
        if s[0] == '-':
            sign = -1
        i += 1
    num = 0
    while i < len(s) and s[i].isdigit():
        num = num * 10 + int(s[i])
        i += 1
    num *= sign
    num = max(min(num, 2**31 - 1), -2**31)
    return num

# Example usage
s = "   -42"
print("String to integer:", myAtoi(s))  # Output: -42
