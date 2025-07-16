"""
LeetCode 2429. Minimize XOR

Given two integers, return the minimum XOR value by rearranging bits.

Constraints:
- 1 <= num1, num2 <= 10^9
"""

def minimizeXor(num1, num2):
    c = bin(num2).count('1')
    bits = [i for i in range(32) if num1 & (1<<i)]
    res = 0
    for i in range(31,-1,-1):
        if c and num1 & (1<<i):
            res |= (1<<i)
            c -= 1
    for i in range(32):
        if c and not (res & (1<<i)):
            res |= (1<<i)
            c -= 1
    return res

# Example usage:
# print(minimizeXor(3,5))  # Output: 3
