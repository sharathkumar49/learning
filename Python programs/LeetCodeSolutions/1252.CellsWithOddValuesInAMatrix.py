"""
1252. Cells with Odd Values in a Matrix

Given n, m, and indices, return the number of cells with odd values in an n x m matrix after performing increment operations.

Constraints:
- 1 <= n, m <= 50
- 1 <= indices.length <= 100
- 0 <= indices[i][0] < n
- 0 <= indices[i][1] < m

Example:
Input: n = 2, m = 3, indices = [[0,1],[1,1]]
Output: 6

"""
def oddCells(n, m, indices):
    rows = [0]*n
    cols = [0]*m
    for r, c in indices:
        rows[r] += 1
        cols[c] += 1
    return sum((rows[i] + cols[j]) % 2 for i in range(n) for j in range(m))

# Example usage
if __name__ == "__main__":
    print(oddCells(2, 3, [[0,1],[1,1]]))  # Output: 6
