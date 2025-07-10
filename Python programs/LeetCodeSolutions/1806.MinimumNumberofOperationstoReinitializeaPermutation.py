"""
LeetCode 1806. Minimum Number of Operations to Reinitialize a Permutation

Given an even integer n, return the minimum number of operations to reinitialize a permutation perm.

Example 1:
Input: n = 2
Output: 1

Constraints:
- 2 <= n <= 1000
- n is even
"""

def reinitializePermutation(n):
    perm = list(range(n))
    arr = list(range(n))
    step = 0
    while True:
        arr = [arr[i//2] if i%2==0 else arr[n//2 + (i-1)//2] for i in range(n)]
        step += 1
        if arr == perm:
            return step

# Example usage:
# n = 2
# print(reinitializePermutation(n))  # Output: 1
