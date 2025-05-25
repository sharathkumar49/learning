# Microsoft: Set Matrix Zeroes
def set_zeroes(matrix):
    m, n = len(matrix), len(matrix[0])
    rows, cols = set(), set()
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:
                rows.add(i)
                cols.add(j)
    for i in range(m):
        for j in range(n):
            if i in rows or j in cols:
                matrix[i][j] = 0
    return matrix

if __name__ == "__main__":
    m = int(input("Rows: "))
    n = int(input("Cols: "))
    matrix = [list(map(int, input().split())) for _ in range(m)]
    print("Zeroed matrix:")
    for row in set_zeroes(matrix):
        print(row)
