"""
1015. Smallest Integer Divisible by K

Given a positive integer K, you need to find the length of the smallest positive integer N such that N is divisible by K, and N only contains the digit 1.

Return the length of N. If there is no such N, return -1.

Constraints:
- 1 <= K <= 10^5

Example:
Input: K = 3
Output: 3
Explanation: The smallest such N is 111, which has length 3.
"""
def smallestRepunitDivByK(K: int) -> int:
    if K % 2 == 0 or K % 5 == 0:
        return -1
    N = 1
    for length in range(1, K+1):
        if N % K == 0:
            return length
        N = (N * 10 + 1) % K
    return -1

# Example usage:
K = 3
print(smallestRepunitDivByK(K))  # Output: 3
