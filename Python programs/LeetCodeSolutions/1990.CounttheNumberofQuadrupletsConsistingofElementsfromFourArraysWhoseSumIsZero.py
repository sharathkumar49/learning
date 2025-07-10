"""
LeetCode 1990. Count the Number of Quadruplets Consisting of Elements from Four Arrays Whose Sum Is Zero

Given four integer arrays A, B, C, D, return the number of quadruplets (i, j, k, l) such that A[i] + B[j] + C[k] + D[l] == 0.

Example:
Input: A = [1,2], B = [-2,-1], C = [-1,2], D = [0,2]
Output: 2

Constraints:
- 1 <= A.length, B.length, C.length, D.length <= 500
- -2^28 <= A[i], B[i], C[i], D[i] <= 2^28
"""

def fourSumCount(A, B, C, D):
    from collections import Counter
    AB = Counter(a+b for a in A for b in B)
    return sum(AB[-c-d] for c in C for d in D)

# Example usage:
# print(fourSumCount([1,2], [-2,-1], [-1,2], [0,2]))  # Output: 2
