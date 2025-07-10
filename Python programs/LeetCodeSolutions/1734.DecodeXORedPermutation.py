"""
LeetCode 1734. Decode XORed Permutation

Given an integer n and an array encoded, where encoded[i] = perm[i] XOR perm[i+1], return the original permutation perm.

Example 1:
Input: encoded = [3,1], n = 3
Output: [1,2,3]

Constraints:
- 3 <= n <= 10^5
- n is odd
- encoded.length == n - 1
"""

def decode(encoded):
    n = len(encoded) + 1
    total = 0
    for i in range(1, n+1):
        total ^= i
    odd = 0
    for i in range(1, len(encoded), 2):
        odd ^= encoded[i]
    perm = [total ^ odd]
    for e in encoded:
        perm.append(perm[-1] ^ e)
    return perm

# Example usage:
# encoded = [3,1]
# print(decode(encoded))  # Output: [1,2,3]
