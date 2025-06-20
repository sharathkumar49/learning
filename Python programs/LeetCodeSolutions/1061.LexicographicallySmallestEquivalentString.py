"""
1061. Lexicographically Smallest Equivalent String

Given two strings A and B of the same length, and a string S, return the lexicographically smallest equivalent string of S by using the equivalence information from A and B.

Constraints:
- 1 <= A.length == B.length <= 1000
- 1 <= S.length <= 1000
- A, B, and S consist of lowercase English letters.

Example:
Input: A = "parker", B = "morris", S = "parser"
Output: "makkek"
"""
def smallestEquivalentString(A: str, B: str, S: str) -> str:
    parent = {chr(i): chr(i) for i in range(ord('a'), ord('z')+1)}
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]
    for a, b in zip(A, B):
        pa, pb = find(a), find(b)
        if pa != pb:
            if pa < pb:
                parent[pb] = pa
            else:
                parent[pa] = pb
    return ''.join(find(c) for c in S)

# Example usage:
A = "parker"
B = "morris"
S = "parser"
print(smallestEquivalentString(A, B, S))  # Output: "makkek"
