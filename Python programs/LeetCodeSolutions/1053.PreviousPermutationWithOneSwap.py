"""
1053. Previous Permutation With One Swap

Given an array of positive integers, return the lexicographically largest permutation that is smaller than the current one, with at most one swap. If no such permutation exists, return the array as is.

Constraints:
- 1 <= A.length <= 10000
- 1 <= A[i] <= 10000

Example:
Input: A = [3,2,1]
Output: [3,1,2]
"""
from typing import List

def prevPermOpt1(A: List[int]) -> List[int]:
    n = len(A)
    for i in range(n-2, -1, -1):
        if A[i] > A[i+1]:
            j = n-1
            while A[j] >= A[i] or (j > 0 and A[j] == A[j-1]):
                j -= 1
            A[i], A[j] = A[j], A[i]
            break
    return A

# Example usage:
A = [3,2,1]
print(prevPermOpt1(A))  # Output: [3, 1, 2]
