"""
LeetCode 760. Find Anagram Mappings

Given two lists A and B, and B is an anagram of A. B is an anagram of A means B is made by randomizing the order of the elements in A.
Return an index mapping P, from A to B. P[i] = j means the i-th element in A appears in B at index j.

Example 1:
Input: A = [12,28,46,32,50], B = [50,12,32,46,28]
Output: [1,4,3,2,0]

Constraints:
- 1 <= A.length == B.length <= 100
- A, B are permutations of each other.
- 0 <= A[i], B[i] < 10^5
"""
from typing import List

def anagramMappings(A: List[int], B: List[int]) -> List[int]:
    idx = {}
    for i, b in enumerate(B):
        idx.setdefault(b, []).append(i)
    res = []
    for a in A:
        res.append(idx[a].pop())
    return res

# Example usage
if __name__ == "__main__":
    print(anagramMappings([12,28,46,32,50], [50,12,32,46,28]))  # Output: [1,4,3,2,0]
