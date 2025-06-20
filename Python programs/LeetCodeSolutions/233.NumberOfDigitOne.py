"""
233. Number of Digit One
https://leetcode.com/problems/number-of-digit-one/

Given an integer n, count the total number of digit 1 appearing in all non-negative integers less than or equal to n.

Constraints:
- 0 <= n <= 10^9

Example 1:
Input: n = 13
Output: 6

Example 2:
Input: n = 0
Output: 0
"""
def countDigitOne(n):
    count = 0
    i = 1
    while i <= n:
        divider = i * 10
        count += (n // divider) * i + min(max(n % divider - i + 1, 0), i)
        i *= 10
    return count

# Example usage:
if __name__ == "__main__":
    print(countDigitOne(13))  # Output: 6
    print(countDigitOne(0))   # Output: 0
