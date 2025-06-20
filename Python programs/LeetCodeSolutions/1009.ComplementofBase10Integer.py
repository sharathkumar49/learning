"""
1009. Complement of Base 10 Integer

Every non-negative integer N has a binary representation. The complement of N is the number in binary you get by flipping all the 0's to 1's and all the 1's to 0's.

Return the complement of N as an integer.

Constraints:
- 0 <= N < 10^9

Example:
Input: N = 5
Output: 2
Explanation: 5 in binary is 101 (base 2). Its complement is 010 (base 2) = 2.
"""
def bitwiseComplement(N: int) -> int:
    if N == 0:
        return 1
    mask = 1
    while mask <= N:
        mask = mask << 1
    return (mask - 1) ^ N

# Example usage:
N = 5
print(bitwiseComplement(N))  # Output: 2
