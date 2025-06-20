"""
1056. Confusing Number

A confusing number is a number that when rotated 180 degrees becomes a different valid number. Return true if the number is confusing.

Constraints:
- 0 <= N <= 10^9

Example:
Input: N = 6
Output: true
"""
def confusingNumber(N: int) -> bool:
    mapping = {0:0, 1:1, 6:9, 8:8, 9:6}
    n, res = N, 0
    while n:
        d = n % 10
        if d not in mapping:
            return False
        res = res * 10 + mapping[d]
        n //= 10
    return res != N

# Example usage:
N = 6
print(confusingNumber(N))  # Output: True
