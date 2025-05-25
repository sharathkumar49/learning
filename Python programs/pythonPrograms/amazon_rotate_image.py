# Amazon: Rotate Image (Matrix)
# Rotate an n x n 2D matrix by 90 degrees (clockwise) in-place.

def rotate(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    for row in matrix:
        row.reverse()
    return matrix

if __name__ == "__main__":
    m1 = [[1,2,3],[4,5,6],[7,8,9]]
    print(rotate([row[:] for row in m1]))  # Output: [[7,4,1],[8,5,2],[9,6,3]]
    m2 = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
    print(rotate([row[:] for row in m2]))  # Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
