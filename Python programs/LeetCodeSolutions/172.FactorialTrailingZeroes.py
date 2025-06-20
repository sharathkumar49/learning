"""
172. Factorial Trailing Zeroes
https://leetcode.com/problems/factorial-trailing-zeroes/

Given an integer n, return the number of trailing zeroes in n!.

Constraints:
- 0 <= n <= 10^4

Example:
Input: n = 5
Output: 1
"""
def trailingZeroes(n: int) -> int:
    count = 0
    while n:
        n //= 5
        count += n
    return count

# Example usage:
if __name__ == "__main__":
    print(trailingZeroes(5))   # Output: 1
    print(trailingZeroes(30))  # Output: 7
