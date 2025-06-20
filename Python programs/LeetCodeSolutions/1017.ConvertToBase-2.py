"""
1017. Convert to Base -2

Given a number N, return a string representing its representation in base -2.

Constraints:
- 0 <= N <= 10^9

Example:
Input: N = 2
Output: "110"
Explanation: (-2)^2 * 1 + (-2)^1 * 1 + (-2)^0 * 0 = 4 - 2 + 0 = 2
"""
def baseNeg2(N: int) -> str:
    if N == 0:
        return "0"
    res = ''
    while N != 0:
        N, r = divmod(N, -2)
        if r < 0:
            N += 1
            r += 2
        res = str(r) + res
    return res

# Example usage:
N = 2
print(baseNeg2(N))  # Output: "110"
