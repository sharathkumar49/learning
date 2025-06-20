"""
870. Advantage Shuffle

Given two arrays A and B of equal size, return any permutation of A that maximizes the number of positions i where A[i] > B[i].

Example 1:
Input: A = [2,7,11,15], B = [1,10,4,11]
Output: [2,11,7,15]

Example 2:
Input: A = [12,24,8,32], B = [13,25,32,11]
Output: [24,32,8,12]

Constraints:
- 1 <= A.length <= 10^5
- A.length == B.length
- 0 <= A[i], B[i] <= 10^9
"""
def advantageCount(A, B):
    A = sorted(A)
    B_idx = sorted(range(len(B)), key=lambda i: B[i])
    res = [0] * len(A)
    j = 0
    for a in A:
        if a > B[B_idx[j]]:
            res[B_idx[j]] = a
            j += 1
        else:
            res[B_idx[-1]] = a
            B_idx.pop()
    return res

# Example usage:
print(advantageCount([2,7,11,15], [1,10,4,11]))  # Output: [2,11,7,15]
print(advantageCount([12,24,8,32], [13,25,32,11]))  # Output: [24,32,8,12]
