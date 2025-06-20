"""
1007. Minimum Domino Rotations For Equal Row

In a row of dominoes, A[i] and B[i] represent the top and bottom halves of the i-th domino. (A domino is a tile with two numbers from 1 to 6 - one on each half of the tile.)

We may rotate the i-th domino, so that A[i] and B[i] swap values.

Return the minimum number of rotations so that all the values in A are the same, or all the values in B are the same.

If it cannot be done, return -1.

Constraints:
- 2 <= A.length == B.length <= 2 * 10^4
- 1 <= A[i], B[i] <= 6

Example:
Input: A = [2,1,2,4,2,2], B = [5,2,6,2,3,2]
Output: 2
Explanation: The first and third dominoes were rotated so that every value in the top row is 2.
"""
from typing import List

def minDominoRotations(A: List[int], B: List[int]) -> int:
    for x in [A[0], B[0]]:
        if all(x == a or x == b for a, b in zip(A, B)):
            return min(len(A) - A.count(x), len(B) - B.count(x))
    return -1

# Example usage:
A = [2,1,2,4,2,2]
B = [5,2,6,2,3,2]
print(minDominoRotations(A, B))  # Output: 2
