"""
LeetCode 738. Monotone Increasing Digits

Given a non-negative integer n, return the largest number that is less than or equal to n with monotone increasing digits.

Example 1:
Input: n = 10
Output: 9

Example 2:
Input: n = 1234
Output: 1234

Example 3:
Input: n = 332
Output: 299

Constraints:
- 0 <= n <= 10^9
"""
def monotoneIncreasingDigits(n: int) -> int:
    digits = list(str(n))
    i = 1
    while i < len(digits) and digits[i-1] <= digits[i]:
        i += 1
    if i < len(digits):
        while i > 0 and digits[i-1] > digits[i]:
            digits[i-1] = str(int(digits[i-1]) - 1)
            i -= 1
        for j in range(i+1, len(digits)):
            digits[j] = '9'
    return int(''.join(digits))

# Example usage
if __name__ == "__main__":
    print(monotoneIncreasingDigits(10))    # Output: 9
    print(monotoneIncreasingDigits(1234))  # Output: 1234
    print(monotoneIncreasingDigits(332))   # Output: 299
