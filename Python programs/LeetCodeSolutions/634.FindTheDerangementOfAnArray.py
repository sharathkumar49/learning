"""
634. Find the Derangement of An Array
Difficulty: Medium

In combinatorial mathematics, a derangement is a permutation of the elements of an array such that no element appears in its original position.
Given an integer n, return the number of derangements of an array of length n. Since the answer may be very large, return it modulo 10^9 + 7.

Example 1:
Input: n = 3
Output: 2

Example 2:
Input: n = 4
Output: 9

Constraints:
1 <= n <= 10^6
"""

def findDerangement(n):
    MOD = 10**9 + 7
    if n == 1:
        return 0
    if n == 2:
        return 1
    a, b = 0, 1
    for i in range(3, n+1):
        a, b = b, (i-1)*(a+b)%MOD
    return b

# Example usage
if __name__ == "__main__":
    print(findDerangement(3))  # Output: 2
    print(findDerangement(4))  # Output: 9
