"""
1060. Missing Element in Sorted Array

Given a sorted array A, return the k-th missing number starting from the first element of A.

Constraints:
- 1 <= A.length <= 5 * 10^4
- 1 <= A[i] <= 10^7
- 1 <= k <= 10^8

Example:
Input: A = [4,7,9,10], k = 1
Output: 5
"""
from typing import List

def missingElement(A: List[int], k: int) -> int:
    n = len(A)
    def missing(idx):
        return A[idx] - A[0] - idx
    if k > missing(n - 1):
        return A[-1] + k - missing(n - 1)
    left, right = 0, n - 1
    while left < right:
        mid = (left + right) // 2
        if missing(mid) < k:
            left = mid + 1
        else:
            right = mid
    return A[left - 1] + k - missing(left - 1)

# Example usage:
A = [4,7,9,10]
k = 1
print(missingElement(A, k))  # Output: 5
