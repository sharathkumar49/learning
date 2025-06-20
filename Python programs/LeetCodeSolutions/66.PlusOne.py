# 66. Plus One
# Given a non-empty array of decimal digits representing a non-negative integer, increment one to the integer.
# The digits are stored such that the most significant digit is at the head of the list, and each element in the array contains a single digit.
#
# Example 1:
# Input: digits = [1,2,3]
# Output: [1,2,4]
#
# Example 2:
# Input: digits = [4,3,2,1]
# Output: [4,3,2,2]
#
# Example 3:
# Input: digits = [9]
# Output: [1,0]
#
# Constraints:
# 1 <= digits.length <= 100
# 0 <= digits[i] <= 9

def plusOne(digits):
    n = len(digits)
    for i in range(n-1, -1, -1):
        if digits[i] < 9:
            digits[i] += 1
            return digits
        digits[i] = 0
    return [1] + digits

# Example usage
digits = [9,9,9]
print("Plus one:", plusOne(digits))  # Output: [1,0,0,0]
