"""
LeetCode 1545. Find Kth Bit in Nth Binary String

Given two integers n and k, return the kth bit in the nth binary string. The nth binary string is defined recursively.

Constraints:
- 1 <= n <= 20
- 1 <= k <= 2^n - 1

Example:
Input: n = 3, k = 1
Output: "0"
"""
def findKthBit(n, k):
    if n == 1:
        return "0"
    l = 2**(n-1)
    if k == l:
        return "1"
    if k < l:
        return findKthBit(n-1, k)
    return str(1 - int(findKthBit(n-1, 2*l-k)))

# Example usage:
n = 3
k = 1
print(findKthBit(n, k))  # Output: "0"
