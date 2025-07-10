"""
LeetCode 1652. Defuse the Bomb

Given a circular array code and an integer k, return the decrypted array.

Example 1:
Input: code = [5,7,1,4], k = 3
Output: [12,10,16,13]

Constraints:
- 1 <= code.length <= 100
- -100 <= code[i] <= 100
- -100 <= k <= 100
"""

def decrypt(code, k):
    n = len(code)
    res = [0]*n
    for i in range(n):
        if k == 0:
            res[i] = 0
        elif k > 0:
            res[i] = sum(code[(i+j)%n] for j in range(1, k+1))
        else:
            res[i] = sum(code[(i-j)%n] for j in range(1, -k+1))
    return res

# Example usage:
# code = [5,7,1,4]
# k = 3
# print(decrypt(code, k))  # Output: [12,10,16,13]
