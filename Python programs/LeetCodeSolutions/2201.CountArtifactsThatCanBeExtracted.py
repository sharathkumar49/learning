"""
LeetCode 2201. Count Artifacts That Can Be Extracted

Given a 2D grid, n x n cells represent digging positions. Given arrays dig representing dig positions [i,j], return the number of complete artifacts that can be extracted.

Example:
Input: n = 2, artifacts = [[0,0,0,0],[0,1,1,1]], dig = [[0,0],[0,1],[1,1]]
Output: 1

Constraints:
- 1 <= n <= 1000
- 1 <= artifacts.length, dig.length <= min(n^2, 10^5)
- 0 <= r1, c1, r2, c2 < n
"""

def digArtifacts(n, artifacts, dig):
    dig_set = set((i, j) for i, j in dig)
    count = 0
    for r1, c1, r2, c2 in artifacts:
        can_extract = True
        for i in range(r1, r2 + 1):
            for j in range(c1, c2 + 1):
                if (i, j) not in dig_set:
                    can_extract = False
                    break
            if not can_extract:
                break
        if can_extract:
            count += 1
    return count

# Example usage:
# print(digArtifacts(2, [[0,0,0,0],[0,1,1,1]], [[0,0],[0,1],[1,1]]))  # Output: 1
