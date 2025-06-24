"""
1137. N-th Tribonacci Number

Return the n-th Tribonacci number.

Constraints:
- 0 <= n <= 37

Example:
Input: n = 4
Output: 4
"""
def tribonacci(n: int) -> int:
    a, b, c = 0, 1, 1
    for _ in range(n):
        a, b, c = b, c, a + b + c
    return a

# Example usage:
n = 4
print(tribonacci(n))  # Output: 4
