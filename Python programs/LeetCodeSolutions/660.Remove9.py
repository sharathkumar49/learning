"""
660. Remove 9
Difficulty: Hard

Start from integer 1, remove any number containing the digit 9. Given n, return the nth number after removing all numbers containing the digit 9.

Example 1:
Input: n = 8
Output: 8

Example 2:
Input: n = 9
Output: 10

Constraints:
1 <= n <= 8 * 10^8
"""

def newInteger(n):
    res = 0
    base = 1
    while n:
        res += (n % 9) * base
        n //= 9
        base *= 10
    return res

# Example usage
if __name__ == "__main__":
    print(newInteger(8))   # Output: 8
    print(newInteger(9))   # Output: 10
