# Amazon: Set Matrix Zeroes
# Given an m x n matrix, if an element is 0, set its entire row and column to 0.

def set_zeroes(matrix):
    rows, cols = len(matrix), len(matrix[0])
    row_zero = False
    for r in range(rows):
        for c in range(cols):
            if matrix[r][c] == 0:
                matrix[0][c] = 0
                if r > 0:
                    matrix[r][0] = 0
                else:
                    row_zero = True
    for r in range(1, rows):
        for c in range(1, cols):
            if matrix[0][c] == 0 or matrix[r][0] == 0:
                matrix[r][c] = 0
    if matrix[0][0] == 0:
        for r in range(rows):
            matrix[r][0] = 0
    if row_zero:
        for c in range(cols):
            matrix[0][c] = 0
    return matrix

if __name__ == "__main__":
    m1 = [[1,1,1],[1,0,1],[1,1,1]]
    print(set_zeroes([row[:] for row in m1]))  # Output: [[1,0,1],[0,0,0],[1,0,1]]
    m2 = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
    print(set_zeroes([row[:] for row in m2]))  # Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
