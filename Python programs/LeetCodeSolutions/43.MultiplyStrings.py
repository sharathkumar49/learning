# 43. Multiply Strings
# Given two non-negative integers num1 and num2 represented as strings, return the product as a string.
#
# Example 1:
# Input: num1 = "2", num2 = "3"
# Output: "6"
#
# Example 2:
# Input: num1 = "123", num2 = "456"
# Output: "56088"
#
# Constraints:
# 1 <= num1.length, num2.length <= 200
# num1 and num2 consist of digits only.
# Both num1 and num2 do not contain any leading zero, except the number 0 itself.

def multiply(num1, num2):
    if num1 == "0" or num2 == "0":
        return "0"
    res = [0] * (len(num1) + len(num2))
    num1, num2 = num1[::-1], num2[::-1]
    for i in range(len(num1)):
        for j in range(len(num2)):
            res[i+j] += int(num1[i]) * int(num2[j])
            res[i+j+1] += res[i+j] // 10
            res[i+j] %= 10
    while len(res) > 1 and res[-1] == 0:
        res.pop()
    return ''.join(map(str, res[::-1]))

# Example usage
num1 = "123"
num2 = "456"
print("Product:", multiply(num1, num2))  # Output: "56088"
