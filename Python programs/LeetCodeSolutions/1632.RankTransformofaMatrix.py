"""
LeetCode 1632. Rank Transform of a Matrix

Given a matrix, return a matrix of the same size where each element is replaced by its rank.

Example 1:
Input: matrix = [[1,2],[3,4]]
Output: [[1,2],[2,3]]

Constraints:
- 1 <= matrix.length, matrix[0].length <= 500
- -10^9 <= matrix[i][j] <= 10^9
"""

def matrixRankTransform(matrix):
    from collections import defaultdict
    m, n = len(matrix), len(matrix[0])
    ans = [[0]*n for _ in range(m)]
    d = defaultdict(list)
    for i in range(m):
        for j in range(n):
            d[matrix[i][j]].append((i,j))
    rank = [0]*(m+n)
    for v in sorted(d):
        parent = list(range(m+n))
        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x
        for i,j in d[v]:
            parent[find(i)] = find(j+m)
        maxrank = {}
        for i,j in d[v]:
            root = find(i)
            maxrank[root] = max(maxrank.get(root,0), rank[i], rank[j+m])
        for i,j in d[v]:
            root = find(i)
            ans[i][j] = maxrank[root]+1
        for i,j in d[v]:
            rank[i] = rank[j+m] = ans[i][j]
    return ans

# Example usage:
# matrix = [[1,2],[3,4]]
# print(matrixRankTransform(matrix))  # Output: [[1,2],[2,3]]
