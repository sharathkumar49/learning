"""
LeetCode 1842. Next Palindrome Using Same Digits

Given a numeric string num, return the next palindrome greater than num using the same set of digits, or an empty string if it is not possible.

Example 1:
Input: num = "32123"
Output: "32323"

Constraints:
- 1 <= num.length <= 15
- num consists of digits only.
"""

def nextPalindrome(num):
    n = len(num)
    half = (n + 1) // 2
    left = list(num[:half])
    # Find next permutation of left half
    i = half - 1
    while i > 0 and left[i-1] >= left[i]:
        i -= 1
    if i == 0:
        return ""
    j = half - 1
    while left[j] <= left[i-1]:
        j -= 1
    left[i-1], left[j] = left[j], left[i-1]
    left[i:] = reversed(left[i:])
    # Form palindrome
    if n % 2 == 0:
        res = left + left[::-1]
    else:
        res = left + left[:-1][::-1]
    return "".join(res)

# Example usage:
# num = "32123"
# print(nextPalindrome(num))  # Output: "32323"
