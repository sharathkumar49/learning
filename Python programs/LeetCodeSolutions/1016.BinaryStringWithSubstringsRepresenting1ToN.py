"""
1016. Binary String With Substrings Representing 1 To N

Given a binary string S and a positive integer N, return true if and only if for every integer X from 1 to N, the binary representation of X is a substring of S.

Constraints:
- 1 <= S.length <= 1000
- 1 <= N <= 10^9

Example:
Input: S = "0110", N = 3
Output: true
Explanation: The binary representations "1", "10", and "11" are all substrings of S.
"""
def queryString(S: str, N: int) -> bool:
    for x in range(N, N//2, -1):
        if bin(x)[2:] not in S:
            return False
    return True

# Example usage:
S = "0110"
N = 3
print(queryString(S, N))  # Output: True
