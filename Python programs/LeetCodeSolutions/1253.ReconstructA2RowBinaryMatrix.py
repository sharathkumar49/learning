"""
1253. Reconstruct a 2-Row Binary Matrix

Given integers upper, lower, and an array colsum, reconstruct a binary matrix with 2 rows that satisfies the row and column sums.

Constraints:
- 1 <= colsum.length <= 10^5
- 0 <= upper, lower <= colsum.length
- 0 <= colsum[i] <= 2

Example:
Input: upper = 2, lower = 1, colsum = [1,1,1]
Output: [[1,1,0],[0,0,1]]

"""
def reconstructMatrix(upper, lower, colsum):
    n = len(colsum)
    res = [[0]*n for _ in range(2)]
    for i, c in enumerate(colsum):
        if c == 2:
            res[0][i] = res[1][i] = 1
            upper -= 1
            lower -= 1
    for i, c in enumerate(colsum):
        if c == 1:
            if upper > 0:
                res[0][i] = 1
                upper -= 1
            else:
                res[1][i] = 1
                lower -= 1
    if upper != 0 or lower != 0:
        return []
    return res

# Example usage
if __name__ == "__main__":
    print(reconstructMatrix(2, 1, [1,1,1]))  # Output: [[1,1,0],[0,0,1]]
