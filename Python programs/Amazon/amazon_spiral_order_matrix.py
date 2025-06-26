# Amazon: Spiral Order Matrix
def spiral_order(matrix):
    res = []
    while matrix:
        res += matrix.pop(0)
        if matrix and matrix[0]:
            for row in matrix:
                res.append(row.pop())
        if matrix:
            res += matrix.pop()[::-1]
        if matrix and matrix[0]:
            for row in matrix[::-1]:
                res.append(row.pop(0))
    return res

if __name__ == "__main__":
    m = int(input("Rows: "))
    n = int(input("Cols: "))
    matrix = [list(map(int, input().split())) for _ in range(m)]
    print("Spiral order:", spiral_order(matrix))
