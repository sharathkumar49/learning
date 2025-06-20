"""
566. Reshape the Matrix
Difficulty: Easy

In MATLAB, there is a handy function called reshape which can reshape an m x n matrix into a new one with a different size r x c keeping its original data.
You are given an m x n matrix mat and two integers r and c representing the number of rows and the number of columns of the wanted reshaped matrix.
The reshaped matrix should be filled with all the elements of the original matrix in the same row-traversing order as they were.
If the reshape operation with given parameters is possible and legal, output the new reshaped matrix; Otherwise, output the original matrix.

Example 1:
Input: mat = [[1,2],[3,4]], r = 1, c = 4
Output: [[1,2,3,4]]

Example 2:
Input: mat = [[1,2],[3,4]], r = 2, c = 4
Output: [[1,2],[3,4]]

Constraints:
1 <= mat.length, mat[i].length <= 100
-1000 <= mat[i][j] <= 1000
1 <= r, c <= 300
"""

def matrixReshape(mat, r, c):
    flat = [num for row in mat for num in row]
    if len(flat) != r * c:
        return mat
    return [flat[i*c:(i+1)*c] for i in range(r)]

# Example usage
if __name__ == "__main__":
    print(matrixReshape([[1,2],[3,4]], 1, 4))  # Output: [[1,2,3,4]]
    print(matrixReshape([[1,2],[3,4]], 2, 4))  # Output: [[1,2],[3,4]]
