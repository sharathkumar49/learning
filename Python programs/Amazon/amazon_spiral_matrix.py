# Amazon: Spiral Matrix
# Given an m x n matrix, return all elements of the matrix in spiral order.

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
    print(spiral_order([[1,2,3],[4,5,6],[7,8,9]]))  # Output: [1,2,3,6,9,8,7,4,5]
    print(spiral_order([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))  # Output: [1,2,3,4,8,12,11,10,9,5,6,7]
