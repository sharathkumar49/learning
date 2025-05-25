# Microsoft: Rotate Image (matrix)
def rotate(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    for row in matrix:
        row.reverse()
    return matrix

if __name__ == "__main__":
    n = int(input("Size of matrix: "))
    matrix = [list(map(int, input().split())) for _ in range(n)]
    print("Rotated matrix:")
    for row in rotate(matrix):
        print(row)
